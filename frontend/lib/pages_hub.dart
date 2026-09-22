import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import 'api.dart';
import 'models.dart';
import 'theme.dart';
import 'widgets.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final _search = TextEditingController();
  List<SportSummary> featured = [];
  List<SportSummary> popular = [];
  List<SportSummary> recent = [];
  List<SportSummary> all = [];
  List<CategoryItem> cats = [];
  String? error;

  @override
  void initState() {
    super.initState();
    _fetch();
  }

  Future<void> _fetch() async {
    try {
      final results = await Future.wait([
        api.sports(featured: true),
        api.sports(popular: true),
        api.sports(),
        api.categories(),
      ]);
      if (!mounted) return;
      setState(() {
        featured = results[0] as List<SportSummary>;
        popular = results[1] as List<SportSummary>;
        all = results[2] as List<SportSummary>;
        recent = List<SportSummary>.from(all)..sort((a, b) => (b.updatedAt ?? '').compareTo(a.updatedAt ?? ''));
        if (recent.length > 6) recent = recent.take(6).toList();
        cats = results[3] as List<CategoryItem>;
      });
    } catch (e) {
      if (!mounted) return;
      setState(() => error = e.toString());
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        Container(
          color: HubColors.navy,
          padding: const EdgeInsets.symmetric(vertical: 48, horizontal: 20),
          child: MaxWidth(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('SPORTS HUB', style: TextStyle(color: HubColors.teal, letterSpacing: 2, fontWeight: FontWeight.w800)),
                const SizedBox(height: 12),
                Text('Everything Athletes Need in One Place',
                    style: Theme.of(context).textTheme.displaySmall?.copyWith(color: Colors.white, fontWeight: FontWeight.w800, height: 1.1)),
                const SizedBox(height: 12),
                const Text('Clear guides to rules, equipment, techniques, terminology, and safety — for athletes, coaches, students, and beginners.',
                    style: TextStyle(color: Color(0xFFC9D6E5), fontSize: 16, height: 1.5)),
                const SizedBox(height: 24),
                TextField(
                  controller: _search,
                  onSubmitted: (v) => context.go('/search?q=${Uri.encodeQueryComponent(v)}'),
                  decoration: InputDecoration(
                    hintText: 'Search sports, rules, terms, equipment, techniques…',
                    prefixIcon: const Icon(Icons.search),
                    suffixIcon: FilledButton(
                      onPressed: () => context.go('/search?q=${Uri.encodeQueryComponent(_search.text)}'),
                      child: const Text('Search'),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
        MaxWidth(
          child: error != null
              ? NoticeBanner(text: 'Could not load sports. Start the Flask API and PostgreSQL, then refresh.\n$error')
              : Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const SectionHeader('Featured sports', subtitle: 'Start with a sport. Each guide uses the same sections.'),
                    SportGrid(sports: featured),
                    const SectionHeader('Popular sports'),
                    SportGrid(sports: popular),
                    const SectionHeader('Recently updated'),
                    SportGrid(sports: recent),
                    const SectionHeader('Sports categories'),
                    Wrap(
                      spacing: 10,
                      runSpacing: 10,
                      children: cats
                          .map(
                            (c) => ActionChip(
                              label: Text('${c.name}${c.sportCount != null ? ' (${c.sportCount})' : ''}'),
                              onPressed: () => context.go('/categories/${c.slug}'),
                            ),
                          )
                          .toList(),
                    ),
                    const SizedBox(height: 28),
                    const SectionHeader('All sports'),
                    SportGrid(sports: all, aspect: 1.05),
                    const SizedBox(height: 24),
                  ],
                ),
        ),
      ],
    );
  }
}

class SportsPage extends StatefulWidget {
  const SportsPage({super.key});
  @override
  State<SportsPage> createState() => _SportsPageState();
}

class _SportsPageState extends State<SportsPage> {
  List<SportSummary> sports = [];
  String? error;
  @override
  void initState() {
    super.initState();
    api.sports().then((v) => setState(() => sports = v)).catchError((e) => setState(() => error = e.toString()));
  }

  @override
  Widget build(BuildContext context) {
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const SectionHeader('Sports', subtitle: 'Choose a sport to open its information page.'),
          if (error != null) NoticeBanner(text: error!),
          SportGrid(sports: sports),
        ]),
      ),
    ]);
  }
}

class CategoriesPage extends StatefulWidget {
  const CategoriesPage({super.key});
  @override
  State<CategoriesPage> createState() => _CategoriesPageState();
}

class _CategoriesPageState extends State<CategoriesPage> {
  List<CategoryItem> items = [];
  @override
  void initState() {
    super.initState();
    api.categories().then((v) => setState(() => items = v));
  }

  @override
  Widget build(BuildContext context) {
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const SectionHeader('Categories', subtitle: 'Filter sports by how they are commonly grouped.'),
          ...items.map(
            (c) => Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: Card(
                child: ListTile(
                  title: Text(c.name, style: const TextStyle(fontWeight: FontWeight.w700)),
                  subtitle: Text(c.description),
                  trailing: Text('${c.sportCount ?? 0}'),
                  onTap: () => context.go('/categories/${c.slug}'),
                ),
              ),
            ),
          ),
        ]),
      ),
    ]);
  }
}

class CategorySportsPage extends StatefulWidget {
  const CategorySportsPage({super.key, required this.slug});
  final String slug;
  @override
  State<CategorySportsPage> createState() => _CategorySportsPageState();
}

class _CategorySportsPageState extends State<CategorySportsPage> {
  List<SportSummary> sports = [];
  @override
  void initState() {
    super.initState();
    api.categorySports(widget.slug).then((v) => setState(() => sports = v));
  }

  @override
  Widget build(BuildContext context) {
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          SectionHeader(widget.slug.replaceAll('-', ' ')),
          SportGrid(sports: sports),
        ]),
      ),
    ]);
  }
}

class RulesHubPage extends StatefulWidget {
  const RulesHubPage({super.key});
  @override
  State<RulesHubPage> createState() => _RulesHubPageState();
}

class _RulesHubPageState extends State<RulesHubPage> {
  List<SportSummary> sports = [];
  @override
  void initState() {
    super.initState();
    api.sports().then((v) => setState(() => sports = v));
  }

  @override
  Widget build(BuildContext context) {
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const SectionHeader('Rules and regulations', subtitle: 'Official rules may vary by governing organisation and competition.'),
          const NoticeBanner(
            text: 'Entries are educational summaries with source organisations. They are not a substitute for the current official rulebook.',
          ),
          const SizedBox(height: 16),
          ...sports.map(
            (s) => Card(
              child: ListTile(
                leading: Icon(sportIcon(s.icon)),
                title: Text('${s.name} rules'),
                subtitle: Text('Source organisation: ${s.governingOrg}'),
                onTap: () => context.go('/sports/${s.slug}?tab=rules'),
              ),
            ),
          ),
        ]),
      ),
    ]);
  }
}

class TrainingPage extends StatefulWidget {
  const TrainingPage({super.key});
  @override
  State<TrainingPage> createState() => _TrainingPageState();
}

class _TrainingPageState extends State<TrainingPage> {
  List<SportSummary> sports = [];
  @override
  void initState() {
    super.initState();
    api.sports().then((v) => setState(() => sports = v));
  }

  @override
  Widget build(BuildContext context) {
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const SectionHeader('Training and techniques', subtitle: 'Beginner-friendly explanations. Not a substitute for a qualified coach.'),
          ...sports.map(
            (s) => Card(
              child: ListTile(
                leading: Icon(sportIcon(s.icon)),
                title: Text(s.name),
                subtitle: const Text('Basic skills, steps, common mistakes, safety reminders'),
                onTap: () => context.go('/sports/${s.slug}?tab=training'),
              ),
            ),
          ),
        ]),
      ),
    ]);
  }
}

class SafetyPage extends StatefulWidget {
  const SafetyPage({super.key});
  @override
  State<SafetyPage> createState() => _SafetyPageState();
}

class _SafetyPageState extends State<SafetyPage> {
  List<dynamic> general = [];
  @override
  void initState() {
    super.initState();
    api.safety().then((v) => setState(() => general = v['general'] as List? ?? []));
  }

  @override
  Widget build(BuildContext context) {
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const SectionHeader('Sports safety', subtitle: 'General educational information. Not personal medical advice.'),
          const NoticeBanner(
            text: 'Stop playing and seek appropriate care for suspected concussion, chest pain, breathing difficulty, or severe injury. Use qualified supervision for children and combat or water sports.',
          ),
          const SizedBox(height: 16),
          ...general.map((item) {
            final map = Map<String, dynamic>.from(item as Map);
            return Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: InfoBlock(title: map['title'] as String? ?? '', body: map['content'] as String? ?? '', badge: map['topic'] as String?),
            );
          }),
        ]),
      ),
    ]);
  }
}

class AboutPage extends StatefulWidget {
  const AboutPage({super.key});
  @override
  State<AboutPage> createState() => _AboutPageState();
}

class _AboutPageState extends State<AboutPage> {
  Map<String, dynamic>? data;
  @override
  void initState() {
    super.initState();
    api.about().then((v) => setState(() => data = v));
  }

  @override
  Widget build(BuildContext context) {
    final d = data;
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const SectionHeader('About Sports Hub'),
          if (d != null) ...[
            InfoBlock(title: 'Purpose', body: d['purpose'] as String? ?? ''),
            const SizedBox(height: 12),
            InfoBlock(title: 'Who it is for', body: ((d['audience'] as List?) ?? []).join(', ')),
            const SizedBox(height: 12),
            InfoBlock(title: 'Features', body: ((d['features'] as List?) ?? []).map((e) => '• $e').join('\n')),
            const SizedBox(height: 12),
            InfoBlock(title: 'Disclaimer', body: d['disclaimer'] as String? ?? ''),
            const SizedBox(height: 12),
            const InfoBlock(
              title: 'Sources and accuracy',
              body:
                  'Each sport lists governing organisations and rule documents. Administrators can update the source and edition when regulations change. Distinguish official-rule summaries, general explanations, training suggestions, and educational safety notes. Do not invent official regulations when updating content.',
            ),
          ],
        ]),
      ),
    ]);
  }
}
