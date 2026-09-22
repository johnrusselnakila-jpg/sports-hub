import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import 'models.dart';
import 'theme.dart';

class AppShell extends StatelessWidget {
  const AppShell({super.key, required this.child});
  final Widget child;

  static const links = [
    ('/', 'Home'),
    ('/sports', 'Sports'),
    ('/categories', 'Categories'),
    ('/rules', 'Rules'),
    ('/training', 'Training'),
    ('/safety', 'Safety'),
    ('/about', 'About'),
  ];

  @override
  Widget build(BuildContext context) {
    final width = MediaQuery.sizeOf(context).width;
    final compact = width < 980;
    final location = GoRouterState.of(context).uri.path;

    return Scaffold(
      appBar: AppBar(
        titleSpacing: 16,
        title: InkWell(
          onTap: () => context.go('/'),
          child: const Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.sports, color: HubColors.teal),
              SizedBox(width: 8),
              Text('Sports Hub'),
            ],
          ),
        ),
        actions: [
          if (!compact)
            ...links.map(
              (link) => TextButton(
                onPressed: () => context.go(link.$1),
                child: Text(
                  link.$2,
                  style: TextStyle(
                    color: location == link.$1 ? HubColors.teal : Colors.white,
                    fontWeight: location == link.$1 ? FontWeight.w700 : FontWeight.w500,
                  ),
                ),
              ),
            ),
          IconButton(
            tooltip: 'Search',
            onPressed: () => context.go('/search'),
            icon: const Icon(Icons.search),
          ),
          IconButton(
            tooltip: 'Saved',
            onPressed: () => context.go('/saved'),
            icon: const Icon(Icons.bookmark_outline),
          ),
          const SizedBox(width: 8),
        ],
      ),
      drawer: compact
          ? Drawer(
              child: ListView(
                children: [
                  const DrawerHeader(
                    decoration: BoxDecoration(color: HubColors.navy),
                    child: Align(
                      alignment: Alignment.bottomLeft,
                      child: Text('Sports Hub', style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.w700)),
                    ),
                  ),
                  ...links.map(
                    (link) => ListTile(
                      title: Text(link.$2),
                      selected: location == link.$1,
                      onTap: () {
                        Navigator.pop(context);
                        context.go(link.$1);
                      },
                    ),
                  ),
                  ListTile(title: const Text('Search'), onTap: () { Navigator.pop(context); context.go('/search'); }),
                  ListTile(title: const Text('Saved'), onTap: () { Navigator.pop(context); context.go('/saved'); }),
                  ListTile(title: const Text('Admin'), onTap: () { Navigator.pop(context); context.go('/admin'); }),
                ],
              ),
            )
          : null,
      body: Column(
        children: [
          Expanded(child: child),
          const SiteFooter(),
        ],
      ),
    );
  }
}

class SiteFooter extends StatelessWidget {
  const SiteFooter({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      color: HubColors.navyDeep,
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 28),
      child: const Column(
        children: [
          Text('Sports Hub', style: TextStyle(color: Colors.white, fontWeight: FontWeight.w700, fontSize: 16)),
          SizedBox(height: 8),
          Text(
            'Educational sports information. Not an official rulebook or medical advice.',
            textAlign: TextAlign.center,
            style: TextStyle(color: Color(0xFFB8C4D4), fontSize: 13),
          ),
          SizedBox(height: 8),
          Text('Home  ·  Sports  ·  Categories  ·  Rules  ·  Training  ·  Safety  ·  About',
              textAlign: TextAlign.center, style: TextStyle(color: Color(0xFF8AA0B8), fontSize: 12)),
        ],
      ),
    );
  }
}

class MaxWidth extends StatelessWidget {
  const MaxWidth({super.key, required this.child, this.padding});
  final Widget child;
  final EdgeInsets? padding;

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: Alignment.topCenter,
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 1180),
        child: Padding(padding: padding ?? const EdgeInsets.all(20), child: child),
      ),
    );
  }
}

class SectionHeader extends StatelessWidget {
  const SectionHeader(this.title, {super.key, this.subtitle});
  final String title;
  final String? subtitle;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16, top: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: Theme.of(context).textTheme.headlineSmall?.copyWith(fontWeight: FontWeight.w800, color: HubColors.ink)),
          if (subtitle != null) ...[
            const SizedBox(height: 6),
            Text(subtitle!, style: const TextStyle(color: Color(0xFF4B5C73))),
          ],
        ],
      ),
    );
  }
}

IconData sportIcon(String? name) {
  switch (name) {
    case 'sports_basketball':
      return Icons.sports_basketball;
    case 'sports_volleyball':
      return Icons.sports_volleyball;
    case 'sports_soccer':
      return Icons.sports_soccer;
    case 'sports_tennis':
      return Icons.sports_tennis;
    case 'pool':
      return Icons.pool;
    case 'directions_run':
      return Icons.directions_run;
    case 'sports_mma':
      return Icons.sports_mma;
    case 'sports_martial_arts':
      return Icons.sports_kabaddi;
    case 'sports_baseball':
      return Icons.sports_baseball;
    case 'directions_bike':
      return Icons.directions_bike;
    default:
      return Icons.sports;
  }
}

class SportCard extends StatelessWidget {
  const SportCard({super.key, required this.sport, this.onTap});
  final SportSummary sport;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    Color accent = HubColors.teal;
    if (sport.accentColor != null) {
      final hex = sport.accentColor!.replaceAll('#', '');
      if (hex.length == 6) {
        accent = Color(int.parse('FF$hex', radix: 16));
      }
    }
    return Card(
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: onTap ?? () => context.go('/sports/${sport.slug}'),
        child: Padding(
          padding: const EdgeInsets.all(18),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              CircleAvatar(
                backgroundColor: accent.withValues(alpha: 0.15),
                foregroundColor: accent,
                child: Icon(sportIcon(sport.icon)),
              ),
              const SizedBox(height: 14),
              Text(sport.name, style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 18)),
              const SizedBox(height: 8),
              Text(sport.tagline, maxLines: 3, overflow: TextOverflow.ellipsis, style: const TextStyle(color: Color(0xFF4B5C73), height: 1.4)),
              const Spacer(),
              const SizedBox(height: 12),
              Text('Open guide →', style: TextStyle(color: accent, fontWeight: FontWeight.w700)),
            ],
          ),
        ),
      ),
    );
  }
}

class SportGrid extends StatelessWidget {
  const SportGrid({super.key, required this.sports, this.aspect = 0.95});
  final List<SportSummary> sports;
  final double aspect;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        var cols = 1;
        if (constraints.maxWidth > 1100) {
          cols = 4;
        } else if (constraints.maxWidth > 800) {
          cols = 3;
        } else if (constraints.maxWidth > 520) {
          cols = 2;
        }
        return GridView.builder(
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          itemCount: sports.length,
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: cols,
            mainAxisSpacing: 16,
            crossAxisSpacing: 16,
            childAspectRatio: aspect,
          ),
          itemBuilder: (context, i) => SportCard(sport: sports[i]),
        );
      },
    );
  }
}

class NoticeBanner extends StatelessWidget {
  const NoticeBanner({super.key, required this.text});
  final String text;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFFFFF4E5),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: const Color(0xFFFFD59E)),
      ),
      child: Text(text, style: const TextStyle(height: 1.45)),
    );
  }
}

class InfoBlock extends StatelessWidget {
  const InfoBlock({super.key, required this.title, required this.body, this.badge});
  final String title;
  final String body;
  final String? badge;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(18),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Expanded(child: Text(title, style: const TextStyle(fontWeight: FontWeight.w800, fontSize: 16))),
                if (badge != null)
                  Chip(label: Text(badge!, style: const TextStyle(fontSize: 11)), visualDensity: VisualDensity.compact),
              ],
            ),
            const SizedBox(height: 8),
            Text(body, style: const TextStyle(height: 1.5, color: Color(0xFF334155))),
          ],
        ),
      ),
    );
  }
}
