import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import 'pages_admin.dart';
import 'pages_detail.dart';
import 'pages_hub.dart';
import 'theme.dart';
import 'widgets.dart';

void main() {
  runApp(const SportsHubApp());
}

final _router = GoRouter(
  routes: [
    ShellRoute(
      builder: (context, state, child) => AppShell(child: child),
      routes: [
        GoRoute(path: '/', builder: (c, s) => const HomePage()),
        GoRoute(path: '/sports', builder: (c, s) => const SportsPage()),
        GoRoute(
          path: '/sports/:slug',
          builder: (c, s) => SportDetailPage(slug: s.pathParameters['slug']!, tab: s.uri.queryParameters['tab']),
        ),
        GoRoute(path: '/categories', builder: (c, s) => const CategoriesPage()),
        GoRoute(path: '/categories/:slug', builder: (c, s) => CategorySportsPage(slug: s.pathParameters['slug']!)),
        GoRoute(path: '/rules', builder: (c, s) => const RulesHubPage()),
        GoRoute(path: '/training', builder: (c, s) => const TrainingPage()),
        GoRoute(path: '/safety', builder: (c, s) => const SafetyPage()),
        GoRoute(path: '/about', builder: (c, s) => const AboutPage()),
        GoRoute(path: '/search', builder: (c, s) => SearchPage(initial: s.uri.queryParameters['q'])),
        GoRoute(path: '/saved', builder: (c, s) => const SavedPage()),
        GoRoute(path: '/admin', builder: (c, s) => const AdminPage()),
      ],
    ),
  ],
);

class SportsHubApp extends StatelessWidget {
  const SportsHubApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Sports Hub',
      debugShowCheckedModeBanner: false,
      theme: buildTheme(),
      routerConfig: _router,
    );
  }
}
