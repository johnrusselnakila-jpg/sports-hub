import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import 'api.dart';
import 'bookmarks.dart';
import 'models.dart';
import 'theme.dart';
import 'widgets.dart';

class SportDetailPage extends StatefulWidget {
  const SportDetailPage({super.key, required this.slug, this.tab});
  final String slug;
  final String? tab;
  @override
  State<SportDetailPage> createState() => _SportDetailPageState();
}

class _SportDetailPageState extends State<SportDetailPage> with SingleTickerProviderStateMixin {
  SportDetail? sport;
  String? error;
  bool saved = false;
  TabController? tabs;

  static const labels = [
    'Overview',
    'History',
    'Rules',
    'Players',
    'Positions',
    'Playing area',
    'Equipment',
    'Scoring',
    'Fouls',
    'Training',
    'Safety',
    'Terms',
    'FAQ',
    'Sources',
  ];

  @override
  void initState() {
    super.initState();
    tabs = TabController(length: labels.length, vsync: this);
    _load();
  }

  Future<void> _load() async {
    try {
      final detail = await api.sport(widget.slug);
      final isSaved = await bookmarks.isSaved(widget.slug);
      if (!mounted) return;
      setState(() {
        sport = detail;
        saved = isSaved;
      });
      final wanted = widget.tab;
      if (wanted == 'rules') tabs?.index = 2;
      if (wanted == 'training') tabs?.index = 9;
    } catch (e) {
      if (!mounted) return;
      setState(() => error = e.toString());
    }
  }

  @override
  void dispose() {
    tabs?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final s = sport;
    if (error != null) {
      return MaxWidth(child: NoticeBanner(text: error!));
    }
    if (s == null) {
      return const Center(child: CircularProgressIndicator());
    }
    return Column(
      children: [
        Container(
          width: double.infinity,
          color: HubColors.navy,
          padding: const EdgeInsets.fromLTRB(20, 24, 20, 0),
          child: MaxWidth(
            padding: EdgeInsets.zero,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    CircleAvatar(backgroundColor: HubColors.teal, child: Icon(sportIcon(s.summary.icon), color: Colors.white)),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(s.summary.name, style: const TextStyle(color: Colors.white, fontSize: 28, fontWeight: FontWeight.w800)),
                          Text(s.summary.tagline, style: const TextStyle(color: Color(0xFFC9D6E5))),
                        ],
                      ),
                    ),
                    FilledButton.tonal(
                      onPressed: () async {
                        await bookmarks.toggle(widget.slug);
                        setState(() => saved = !saved);
                      },
                      child: Text(saved ? 'Saved' : 'Save'),
                    ),
                  ],
                ),
                const SizedBox(height: 16),
                TabBar(
                  controller: tabs,
                  isScrollable: true,
                  labelColor: HubColors.teal,
                  unselectedLabelColor: Colors.white70,
                  tabs: labels.map((e) => Tab(text: e)).toList(),
                ),
              ],
            ),
          ),
        ),
        Expanded(
          child: TabBarView(
            controller: tabs,
            children: [
              _scroll([InfoBlock(title: 'Overview', body: s.overview), const SizedBox(height: 12), NoticeBanner(text: 'Educational information. Confirm official rules with the listed governing organisation.')]),
              _scroll([InfoBlock(title: 'History', body: s.history)]),
              _scroll([
                const NoticeBanner(text: 'Official rules may vary depending on the governing organisation or competition. Source and edition are listed on each item when available.'),
                const SizedBox(height: 12),
                ...s.rules.asMap().entries.map((e) => Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: InfoBlock(
                        title: '${e.key + 1}. ${e.value.title}',
                        body: '${e.value.content}\n\nSource: ${e.value.sourceOrg ?? 'See references'}\nRule edition: ${e.value.ruleEdition ?? 'Verify current edition'}\nType: ${e.value.contentType}',
                        badge: e.value.contentType,
                      ),
                    )),
              ]),
              _scroll([InfoBlock(title: 'Number of players', body: s.playerCount)]),
              _scroll(s.positions.map((p) => Padding(padding: const EdgeInsets.only(bottom: 12), child: InfoBlock(title: p.name, body: p.description))).toList()),
              _scroll([InfoBlock(title: 'Court / field / course dimensions', body: s.courtDimensions)]),
              _scroll(s.equipment
                  .map((e) => Padding(
                        padding: const EdgeInsets.only(bottom: 12),
                        child: InfoBlock(
                          title: e.name,
                          body: 'Purpose: ${e.purpose}\n\nBasic specifications: ${e.specifications ?? 'See competition rules.'}\n\nSafety: ${e.safety ?? 'Use equipment in good condition.'}',
                        ),
                      ))
                  .toList()),
              _scroll([InfoBlock(title: 'Scoring system', body: s.scoringSystem)]),
              _scroll([
                ...s.fouls.map((f) => Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: InfoBlock(title: f.name, body: f.description, badge: f.kind),
                    )),
                const SizedBox(height: 8),
                const InfoBlock(
                  title: 'Referee signals',
                  body: 'Officials use standardised signals published by the governing organisation. Use the current signal chart from the source listed under Sources — do not rely on informal memory for officiating.',
                ),
              ]),
              _scroll([
                const NoticeBanner(text: 'Training suggestions are beginner-oriented and do not replace a qualified coach or medical professional.'),
                const SizedBox(height: 12),
                ...s.techniques.map((t) => Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: InfoBlock(
                        title: t.name,
                        body: '${t.description}\n\nBasic steps:\n${t.steps.asMap().entries.map((e) => '${e.key + 1}. ${e.value}').join('\n')}\n\nBeginner tips: ${t.beginnerTips ?? '—'}\n\nCommon mistakes: ${t.commonMistakes ?? '—'}\n\nSafety reminders: ${t.safetyReminders ?? '—'}',
                      ),
                    )),
              ]),
              _scroll(s.safety.map((g) => Padding(padding: const EdgeInsets.only(bottom: 12), child: InfoBlock(title: g.name, body: g.description))).toList()),
              _scroll(s.terminology.map((t) => Padding(padding: const EdgeInsets.only(bottom: 12), child: InfoBlock(title: t.name, body: t.description))).toList()),
              _scroll(s.faqs.map((t) => Padding(padding: const EdgeInsets.only(bottom: 12), child: InfoBlock(title: t.name, body: t.description))).toList()),
              _scroll([
                InfoBlock(title: 'Official governing organisation', body: s.summary.governingOrg),
                const SizedBox(height: 12),
                ...s.references.map((r) => Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: InfoBlock(
                        title: r['organization'] as String? ?? 'Source',
                        body: '${r['title']}\nEdition/year: ${r['edition_year'] ?? 'Verify current'}\n${r['url'] ?? ''}\n${r['notes'] ?? ''}',
                      ),
                    )),
              ]),
            ],
          ),
        ),
      ],
    );
  }

  Widget _scroll(List<Widget> children) {
    return ListView(padding: const EdgeInsets.symmetric(vertical: 8), children: [MaxWidth(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: children))]);
  }
}

class SearchPage extends StatefulWidget {
  const SearchPage({super.key, this.initial});
  final String? initial;
  @override
  State<SearchPage> createState() => _SearchPageState();
}

class _SearchPageState extends State<SearchPage> {
  late final TextEditingController _controller;
  List<SearchHit> hits = [];
  String? message;
  bool loading = false;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController(text: widget.initial ?? '');
    if ((_controller.text).length >= 2) {
      _run(_controller.text);
    }
  }

  Future<void> _run(String q) async {
    setState(() {
      loading = true;
      message = null;
    });
    try {
      final data = await api.search(q);
      final list = (data['results'] as List? ?? []).map((e) => SearchHit.fromJson(Map<String, dynamic>.from(e as Map))).toList();
      setState(() {
        hits = list;
        message = list.isEmpty ? (data['message'] as String? ?? 'No results found.') : null;
        loading = false;
      });
    } catch (e) {
      setState(() {
        loading = false;
        message = e.toString();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const SectionHeader('Search', subtitle: 'Find sports, rules, terms, equipment, techniques, and safety notes.'),
          TextField(
            controller: _controller,
            onSubmitted: _run,
            decoration: InputDecoration(
              hintText: 'Try “traveling” or “serve”',
              prefixIcon: const Icon(Icons.search),
              suffixIcon: IconButton(onPressed: () => _run(_controller.text), icon: const Icon(Icons.arrow_forward)),
            ),
          ),
          const SizedBox(height: 20),
          if (loading) const Center(child: CircularProgressIndicator()),
          if (!loading && message != null) NoticeBanner(text: message!),
          if (!loading)
            ...hits.map(
              (h) => Card(
                child: ListTile(
                  title: Text(h.title),
                  subtitle: Text('${h.type} · ${h.sportName ?? ''}\n${h.snippet}', maxLines: 4),
                  isThreeLine: true,
                  onTap: h.sportSlug == null ? null : () => context.go('/sports/${h.sportSlug}'),
                ),
              ),
            ),
        ]),
      ),
    ]);
  }
}
