import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import 'api.dart';
import 'bookmarks.dart';
import 'guide_visuals.dart';
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
                  tabs: labels
                      .map(
                        (e) => Tab(
                          icon: Icon(sectionIcon(e), size: 18),
                          text: e,
                          height: 58,
                        ),
                      )
                      .toList(),
                ),
              ],
            ),
          ),
        ),
        Expanded(
          child: TabBarView(
            controller: tabs,
            children: [
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: '${s.summary.name} at a glance',
                  icon: sportIcon(s.summary.icon),
                  caption: 'Illustrated overview of the playing space',
                  diagram: SportPitchDiagram(slug: s.summary.slug),
                ),
                InfoBlock(title: 'Overview', body: s.overview),
                const SizedBox(height: 12),
                const NoticeBanner(text: 'Educational information. Confirm official rules with the listed governing organisation.'),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'How the sport grew',
                  icon: Icons.history_edu,
                  caption: 'A visual timeline of origin and governing bodies',
                  diagram: IconFactGrid(items: [
                    (Icons.flag, 'Origins', 'See the history text for the founding story and early code.'),
                    (Icons.public, 'International play', s.summary.governingOrg),
                    (Icons.emoji_events, 'Competition', 'Olympic, world, and school events use their own adopted rulebooks.'),
                  ]),
                ),
                InfoBlock(title: 'History', body: s.history),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Rules map',
                  icon: Icons.gavel,
                  caption: 'Each card is one topic — not the full official text',
                  diagram: IconFactGrid(
                    items: s.rules.take(6).map((r) => (Icons.rule, r.title, 'Educational summary with a listed source.')).toList(),
                  ),
                ),
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
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Who is on the field',
                  icon: Icons.groups,
                  caption: 'Typical numbers — competitions may differ',
                  diagram: IconFactGrid(items: [
                    (Icons.people_alt, 'On the field / court', s.playerCount.length > 90 ? '${s.playerCount.substring(0, 90)}…' : s.playerCount),
                    (Icons.event_seat, 'Bench / extras', 'Substitutes and roster size follow the event regulations.'),
                    (Icons.sports, 'Formats', 'Small-sided or age-group versions often use fewer players.'),
                  ]),
                ),
                InfoBlock(title: 'Number of players', body: s.playerCount),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Where players stand',
                  icon: Icons.grid_view,
                  caption: 'Labels are common role names, not a required formation',
                  diagram: PositionBoard(slug: s.summary.slug, names: s.positions.map((p) => p.name).toList()),
                ),
                ...s.positions.map((p) => Padding(padding: const EdgeInsets.only(bottom: 12), child: InfoBlock(title: p.name, body: p.description))),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Playing area diagram',
                  icon: Icons.map_outlined,
                  caption: 'Schematic lines to help you read the written dimensions',
                  diagram: SportPitchDiagram(slug: s.summary.slug, height: 260),
                ),
                InfoBlock(title: 'Court / field / course dimensions', body: s.courtDimensions),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Gear gallery',
                  icon: Icons.inventory_2_outlined,
                  caption: 'Icons stand in for photos — check the written specs',
                  diagram: IconFactGrid(
                    items: s.equipment
                        .map((e) => (_equipIcon(e.name), e.name, e.purpose))
                        .toList(),
                  ),
                ),
                ...s.equipment.map((e) => Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: InfoBlock(
                        title: e.name,
                        body: 'Purpose: ${e.purpose}\n\nBasic specifications: ${e.specifications ?? 'See competition rules.'}\n\nSafety: ${e.safety ?? 'Use equipment in good condition.'}',
                      ),
                    )),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'How points are won',
                  icon: Icons.scoreboard_outlined,
                  caption: 'A visual reminder — values come from the competition rules',
                  diagram: IconFactGrid(items: [
                    (Icons.looks_one, 'Score unit', 'Goals, points, games, or time — see the text below.'),
                    (Icons.timer, 'Match length', 'Periods, sets, innings, or races are defined by the event.'),
                    (Icons.emoji_events, 'Winner', 'Usually most points, fastest time, or required sets/games.'),
                  ]),
                ),
                InfoBlock(title: 'Scoring system', body: s.scoringSystem),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Fouls, violations, signals',
                  icon: Icons.front_hand_outlined,
                  caption: 'Learn the idea, then use the official signal chart',
                  diagram: IconFactGrid(
                    items: s.fouls.take(6).map((f) => (Icons.report, f.name, f.description)).toList(),
                  ),
                ),
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
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Skills in pictures',
                  icon: Icons.fitness_center,
                  caption: 'Each tile is a beginner skill from this sport',
                  diagram: IconFactGrid(
                    items: s.techniques.map((t) => (Icons.sports, t.name, t.description)).toList(),
                  ),
                ),
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
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Stay safer',
                  icon: Icons.health_and_safety_outlined,
                  caption: 'General reminders — not personal medical advice',
                  diagram: IconFactGrid(items: const [
                    (Icons.whatshot, 'Warm-up', 'Prepare joints and raise heart rate before play.'),
                    (Icons.water_drop, 'Hydration', 'Drink according to thirst, climate, and session length.'),
                    (Icons.personal_injury, 'Stop if needed', 'Chest pain, concussion signs, or severe pain means stop.'),
                  ]),
                ),
                ...s.safety.map((g) => Padding(padding: const EdgeInsets.only(bottom: 12), child: InfoBlock(title: g.name, body: g.description))),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Language of the sport',
                  icon: Icons.menu_book_outlined,
                  caption: 'Terms matched to this sport’s diagram',
                  diagram: SportPitchDiagram(slug: s.summary.slug),
                ),
                ...s.terminology.map((t) => Padding(padding: const EdgeInsets.only(bottom: 12), child: InfoBlock(title: t.name, body: t.description))),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Common questions',
                  icon: Icons.help_outline,
                  caption: 'Short answers with the same visual language as the guide',
                  diagram: IconFactGrid(
                    items: s.faqs.take(6).map((t) => (Icons.quiz, t.name, t.description)).toList(),
                  ),
                ),
                ...s.faqs.map((t) => Padding(padding: const EdgeInsets.only(bottom: 12), child: InfoBlock(title: t.name, body: t.description))),
              ]),
              _scroll([
                SectionVisual(
                  slug: s.summary.slug,
                  title: 'Where the rules live',
                  icon: Icons.source_outlined,
                  caption: 'Governing organisations publish the official documents',
                  diagram: IconFactGrid(items: [
                    (Icons.account_balance, 'Governing body', s.summary.governingOrg),
                    (Icons.menu_book, 'Rulebook', 'Confirm the current edition before officiating or competing.'),
                    (Icons.link, 'Updates', 'Administrators can change source and year when regulations change.'),
                  ]),
                ),
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

IconData _equipIcon(String name) {
  final n = name.toLowerCase();
  if (n.contains('ball') && n.contains('basket')) return Icons.sports_basketball;
  if (n.contains('volley')) return Icons.sports_volleyball;
  if (n.contains('football') || n.contains('soccer')) return Icons.sports_soccer;
  if (n.contains('shuttle') || n.contains('racquet') || n.contains('racket')) return Icons.sports_tennis;
  if (n.contains('net')) return Icons.horizontal_rule;
  if (n.contains('shoe') || n.contains('boot')) return Icons.ice_skating_outlined;
  if (n.contains('helmet')) return Icons.sports_motorsports;
  if (n.contains('glove')) return Icons.front_hand;
  if (n.contains('bat')) return Icons.sports_baseball;
  if (n.contains('bike') || n.contains('bicycle')) return Icons.directions_bike;
  if (n.contains('goggle') || n.contains('cap') || n.contains('suit')) return Icons.pool;
  if (n.contains('uniform') || n.contains('dobok') || n.contains('jersey')) return Icons.checkroom;
  return Icons.inventory_2_outlined;
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
