import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import 'api.dart';
import 'bookmarks.dart';
import 'models.dart';
import 'widgets.dart';

class SavedPage extends StatefulWidget {
  const SavedPage({super.key});
  @override
  State<SavedPage> createState() => _SavedPageState();
}

class _SavedPageState extends State<SavedPage> {
  List<SportSummary> saved = [];

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final slugs = await bookmarks.slugs();
    final all = await api.sports();
    setState(() => saved = all.where((s) => slugs.contains(s.slug)).toList());
  }

  @override
  Widget build(BuildContext context) {
    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          const SectionHeader('Saved sports', subtitle: 'Bookmarks are stored in this browser. No account is required.'),
          if (saved.isEmpty) const NoticeBanner(text: 'You have not saved any sports yet. Open a sport and tap Save.'),
          SportGrid(sports: saved),
        ]),
      ),
    ]);
  }
}

class AdminPage extends StatefulWidget {
  const AdminPage({super.key});
  @override
  State<AdminPage> createState() => _AdminPageState();
}

class _AdminPageState extends State<AdminPage> {
  Map<String, dynamic>? user;
  final email = TextEditingController();
  final password = TextEditingController();
  List<SportSummary> sports = [];
  String? error;

  @override
  void initState() {
    super.initState();
    api.me().then((u) {
      setState(() => user = u);
      if (u?['role'] == 'admin') {
        api.sports().then((s) => setState(() => sports = s));
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    if (user == null || user?['role'] != 'admin') {
      return ListView(children: [
        MaxWidth(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            const SectionHeader('Administrator sign in'),
            if (error != null) NoticeBanner(text: error!),
            TextField(controller: email, decoration: const InputDecoration(labelText: 'Email')),
            const SizedBox(height: 12),
            TextField(controller: password, obscureText: true, decoration: const InputDecoration(labelText: 'Password')),
            const SizedBox(height: 16),
            FilledButton(
              onPressed: () async {
                try {
                  final u = await api.login(email.text.trim(), password.text);
                  setState(() {
                    user = u;
                    error = null;
                  });
                  if (u['role'] != 'admin') {
                    setState(() => error = 'This account is not an administrator.');
                    return;
                  }
                  sports = await api.sports();
                  setState(() {});
                } catch (e) {
                  setState(() => error = e.toString());
                }
              },
              child: const Text('Sign in'),
            ),
          ]),
        ),
      ]);
    }

    return ListView(children: [
      MaxWidth(
        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          SectionHeader('Admin dashboard', subtitle: 'Signed in as ${user!['email']}'),
          Wrap(spacing: 8, children: [
            FilledButton.tonal(onPressed: () => _sportDialog(), child: const Text('Add sport')),
            OutlinedButton(
              onPressed: () async {
                await api.logout();
                setState(() => user = null);
              },
              child: const Text('Log out'),
            ),
          ]),
          const SizedBox(height: 16),
          const NoticeBanner(text: 'Visitors cannot reach these actions without an admin token. When you edit rules, always store the source organisation and rule edition/year.'),
          const SizedBox(height: 16),
          ...sports.map(
            (s) => Card(
              child: ListTile(
                title: Text(s.name),
                subtitle: Text(s.governingOrg),
                trailing: Wrap(children: [
                  TextButton(onPressed: () => context.go('/sports/${s.slug}'), child: const Text('View')),
                  TextButton(onPressed: () => _sportDialog(existing: s), child: const Text('Edit')),
                  TextButton(
                    onPressed: () => _childSheet(s, 'rules', ['title', 'content', 'source_org', 'rule_edition', 'content_type']),
                    child: const Text('Rules'),
                  ),
                  TextButton(
                    onPressed: () => _childSheet(s, 'equipment', ['name', 'purpose', 'specifications', 'safety_considerations']),
                    child: const Text('Equipment'),
                  ),
                  TextButton(
                    onPressed: () => _childSheet(s, 'techniques', ['name', 'description', 'beginner_tips', 'common_mistakes', 'safety_reminders']),
                    child: const Text('Techniques'),
                  ),
                  TextButton(
                    onPressed: () => _childSheet(s, 'references', ['organization', 'title', 'edition_year', 'url', 'notes']),
                    child: const Text('Sources'),
                  ),
                  IconButton(
                    onPressed: () async {
                      await api.adminDelete('/api/admin/sports/${s.id}');
                      sports = await api.sports();
                      setState(() {});
                    },
                    icon: const Icon(Icons.delete_outline),
                  ),
                ]),
              ),
            ),
          ),
        ]),
      ),
    ]);
  }

  Future<void> _sportDialog({SportSummary? existing}) async {
    final name = TextEditingController(text: existing?.name ?? '');
    final tagline = TextEditingController(text: existing?.tagline ?? '');
    final overview = TextEditingController(text: existing?.overview ?? '');
    final history = TextEditingController();
    final players = TextEditingController();
    final court = TextEditingController();
    final scoring = TextEditingController();
    final org = TextEditingController(text: existing?.governingOrg ?? '');
    await showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text(existing == null ? 'Add sport' : 'Edit ${existing.name}'),
        content: SizedBox(
          width: 460,
          child: SingleChildScrollView(
            child: Column(children: [
              TextField(controller: name, decoration: const InputDecoration(labelText: 'Name')),
              TextField(controller: tagline, decoration: const InputDecoration(labelText: 'Tagline')),
              TextField(controller: overview, maxLines: 3, decoration: const InputDecoration(labelText: 'Overview')),
              if (existing == null) ...[
                TextField(controller: history, maxLines: 2, decoration: const InputDecoration(labelText: 'History')),
                TextField(controller: players, decoration: const InputDecoration(labelText: 'Number of players')),
                TextField(controller: court, decoration: const InputDecoration(labelText: 'Court / field')),
                TextField(controller: scoring, decoration: const InputDecoration(labelText: 'Scoring')),
              ],
              TextField(controller: org, decoration: const InputDecoration(labelText: 'Governing organisation')),
            ]),
          ),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text('Cancel')),
          FilledButton(
            onPressed: () async {
              try {
                if (existing == null) {
                  await api.adminPost('/api/admin/sports', {
                    'name': name.text,
                    'tagline': tagline.text,
                    'overview': overview.text,
                    'history': history.text,
                    'player_count': players.text,
                    'court_dimensions': court.text,
                    'scoring_system': scoring.text,
                    'governing_org': org.text,
                  });
                } else {
                  await api.adminPut('/api/admin/sports/${existing.id}', {
                    'name': name.text,
                    'tagline': tagline.text,
                    'overview': overview.text,
                    'governing_org': org.text,
                  });
                }
                if (ctx.mounted) Navigator.pop(ctx);
                sports = await api.sports();
                setState(() {});
              } catch (e) {
                setState(() => error = e.toString());
              }
            },
            child: const Text('Save'),
          ),
        ],
      ),
    );
  }

  Future<void> _childSheet(SportSummary sport, String kind, List<String> fields) async {
    final controllers = {for (final f in fields) f: TextEditingController()};
    await showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      builder: (ctx) => Padding(
        padding: EdgeInsets.fromLTRB(20, 20, 20, 20 + MediaQuery.viewInsetsOf(ctx).bottom),
        child: SingleChildScrollView(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('Add $kind to ${sport.name}', style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 18)),
            const SizedBox(height: 12),
            ...fields.map((f) => Padding(
                  padding: const EdgeInsets.only(bottom: 8),
                  child: TextField(controller: controllers[f], maxLines: f.contains('content') || f.contains('notes') ? 3 : 1, decoration: InputDecoration(labelText: f)),
                )),
            FilledButton(
              onPressed: () async {
                final body = {for (final f in fields) f: controllers[f]!.text, 'sport_id': sport.id};
                await api.adminPost('/api/admin/$kind', body);
                if (ctx.mounted) Navigator.pop(ctx);
              },
              child: const Text('Add'),
            ),
          ]),
        ),
      ),
    );
  }
}
