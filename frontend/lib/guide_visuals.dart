import 'package:flutter/material.dart';

import 'theme.dart';

class SectionVisual extends StatelessWidget {
  const SectionVisual({
    super.key,
    required this.slug,
    required this.title,
    required this.icon,
    required this.caption,
    this.diagram,
  });

  final String slug;
  final String title;
  final IconData icon;
  final String caption;
  final Widget? diagram;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Card(
        clipBehavior: Clip.antiAlias,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Container(
              height: 92,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: [HubColors.navy, HubColors.navy.withValues(alpha: 0.85), HubColors.teal.withValues(alpha: 0.85)],
                ),
              ),
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: Row(
                children: [
                  CircleAvatar(
                    radius: 28,
                    backgroundColor: Colors.white,
                    child: Icon(icon, color: HubColors.navy, size: 30),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(title, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w800, fontSize: 18)),
                        Text(caption, style: const TextStyle(color: Color(0xFFD5E4F0), fontSize: 13)),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            if (diagram != null)
              Padding(
                padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
                child: diagram!,
              ),
            const Padding(
              padding: EdgeInsets.fromLTRB(16, 0, 16, 12),
              child: Text(
                'Educational graphic — not an official scaled drawing.',
                style: TextStyle(fontSize: 11, color: Color(0xFF64748B)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class SportPitchDiagram extends StatelessWidget {
  const SportPitchDiagram({super.key, required this.slug, this.height = 220});
  final String slug;
  final double height;

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: slug == 'swimming' || slug == 'athletics' ? 1.7 : 1.55,
      child: CustomPaint(
        painter: _PitchPainter(slug),
        child: const SizedBox.expand(),
      ),
    );
  }
}

class _PitchPainter extends CustomPainter {
  _PitchPainter(this.slug);
  final String slug;

  @override
  void paint(Canvas canvas, Size size) {
    final wood = Paint()..color = const Color(0xFFC9783A);
    final grass = Paint()..color = const Color(0xFF3D8B5F);
    final clay = Paint()..color = const Color(0xFFC46A3A);
    final water = Paint()..color = const Color(0xFF1D6FA3);
    final mat = Paint()..color = const Color(0xFF2C3E50);
    final line = Paint()
      ..color = Colors.white
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.8;
    final fillLine = Paint()..color = Colors.white.withValues(alpha: 0.9);

    final r = RRect.fromRectAndRadius(Offset.zero & size, const Radius.circular(12));
    canvas.clipRRect(r);

    switch (slug) {
      case 'basketball':
        canvas.drawRect(Offset.zero & size, wood);
        _basketball(canvas, size, line, fillLine);
        break;
      case 'volleyball':
        canvas.drawRect(Offset.zero & size, Paint()..color = const Color(0xFFD9A441));
        _volleyball(canvas, size, line);
        break;
      case 'football':
      case 'futsal':
        canvas.drawRect(Offset.zero & size, grass);
        _football(canvas, size, line, fiveASide: slug == 'futsal');
        break;
      case 'tennis':
        canvas.drawRect(Offset.zero & size, clay);
        _tennis(canvas, size, line);
        break;
      case 'badminton':
        canvas.drawRect(Offset.zero & size, Paint()..color = const Color(0xFF2E7D4F));
        _badminton(canvas, size, line);
        break;
      case 'table-tennis':
        canvas.drawRect(Offset.zero & size, Paint()..color = const Color(0xFF1B4F72));
        _tableTennis(canvas, size, line);
        break;
      case 'swimming':
        canvas.drawRect(Offset.zero & size, water);
        _pool(canvas, size, line, fillLine);
        break;
      case 'athletics':
        canvas.drawRect(Offset.zero & size, Paint()..color = const Color(0xFF8B3A3A));
        _track(canvas, size, line);
        break;
      case 'boxing':
        canvas.drawRect(Offset.zero & size, Paint()..color = const Color(0xFF4A3728));
        _ring(canvas, size, line, octagon: false);
        break;
      case 'taekwondo':
        canvas.drawRect(Offset.zero & size, mat);
        _ring(canvas, size, line, octagon: true);
        break;
      case 'baseball':
      case 'softball':
        canvas.drawRect(Offset.zero & size, grass);
        _diamond(canvas, size, line, fillLine);
        break;
      case 'cycling':
        canvas.drawRect(Offset.zero & size, Paint()..color = const Color(0xFF4B5563));
        _loop(canvas, size, line);
        break;
      default:
        canvas.drawRect(Offset.zero & size, Paint()..color = HubColors.navy);
        canvas.drawRect(Rect.fromLTWH(size.width * 0.1, size.height * 0.15, size.width * 0.8, size.height * 0.7), line);
    }
  }

  void _basketball(Canvas canvas, Size size, Paint line, Paint fill) {
    final court = Rect.fromLTWH(size.width * 0.06, size.height * 0.12, size.width * 0.88, size.height * 0.76);
    canvas.drawRect(court, line);
    canvas.drawLine(Offset(court.center.dx, court.top), Offset(court.center.dx, court.bottom), line);
    canvas.drawCircle(court.center, court.height * 0.12, line);
    final keyW = court.width * 0.18;
    final keyH = court.height * 0.36;
    canvas.drawRect(Rect.fromCenter(center: Offset(court.center.dx, court.top + keyH / 2), width: keyW, height: keyH), line);
    canvas.drawRect(Rect.fromCenter(center: Offset(court.center.dx, court.bottom - keyH / 2), width: keyW, height: keyH), line);
    canvas.drawArc(Rect.fromCircle(center: Offset(court.center.dx, court.top + keyH), radius: keyW * 0.55), 0, 3.14, false, line);
    canvas.drawArc(Rect.fromCircle(center: Offset(court.center.dx, court.bottom - keyH), radius: keyW * 0.55), 3.14, 3.14, false, line);
    canvas.drawCircle(Offset(court.center.dx, court.top + 10), 6, fill);
    canvas.drawCircle(Offset(court.center.dx, court.bottom - 10), 6, fill);
  }

  void _volleyball(Canvas canvas, Size size, Paint line) {
    final court = Rect.fromLTWH(size.width * 0.08, size.height * 0.18, size.width * 0.84, size.height * 0.64);
    canvas.drawRect(court, line);
    canvas.drawLine(Offset(court.center.dx, court.top), Offset(court.center.dx, court.bottom), line..strokeWidth = 3);
    final attack = court.width * 0.17;
    canvas.drawLine(Offset(court.center.dx - attack, court.top), Offset(court.center.dx - attack, court.bottom), line..strokeWidth = 1.6);
    canvas.drawLine(Offset(court.center.dx + attack, court.top), Offset(court.center.dx + attack, court.bottom), line);
  }

  void _football(Canvas canvas, Size size, Paint line, {required bool fiveASide}) {
    final pitch = Rect.fromLTWH(size.width * 0.06, size.height * 0.14, size.width * 0.88, size.height * 0.72);
    canvas.drawRRect(RRect.fromRectAndRadius(pitch, const Radius.circular(8)), line);
    canvas.drawLine(Offset(pitch.center.dx, pitch.top), Offset(pitch.center.dx, pitch.bottom), line);
    canvas.drawCircle(pitch.center, pitch.height * 0.12, line);
    final boxW = fiveASide ? pitch.width * 0.16 : pitch.width * 0.18;
    final boxH = fiveASide ? pitch.height * 0.42 : pitch.height * 0.5;
    canvas.drawRect(Rect.fromCenter(center: Offset(pitch.left + boxW / 2, pitch.center.dy), width: boxW, height: boxH), line);
    canvas.drawRect(Rect.fromCenter(center: Offset(pitch.right - boxW / 2, pitch.center.dy), width: boxW, height: boxH), line);
  }

  void _tennis(Canvas canvas, Size size, Paint line) {
    final court = Rect.fromLTWH(size.width * 0.18, size.height * 0.08, size.width * 0.64, size.height * 0.84);
    canvas.drawRect(court, line);
    canvas.drawLine(Offset(court.left, court.center.dy), Offset(court.right, court.center.dy), line..strokeWidth = 2.4);
    canvas.drawLine(Offset(court.center.dx, court.top + court.height * 0.18), Offset(court.center.dx, court.bottom - court.height * 0.18), line..strokeWidth = 1.6);
    canvas.drawLine(Offset(court.left, court.top + court.height * 0.18), Offset(court.right, court.top + court.height * 0.18), line);
    canvas.drawLine(Offset(court.left, court.bottom - court.height * 0.18), Offset(court.right, court.bottom - court.height * 0.18), line);
  }

  void _badminton(Canvas canvas, Size size, Paint line) {
    final court = Rect.fromLTWH(size.width * 0.22, size.height * 0.08, size.width * 0.56, size.height * 0.84);
    canvas.drawRect(court, line);
    canvas.drawLine(Offset(court.left, court.center.dy), Offset(court.right, court.center.dy), line..strokeWidth = 2.5);
    canvas.drawLine(Offset(court.center.dx, court.top), Offset(court.center.dx, court.bottom), line..strokeWidth = 1.5);
    canvas.drawLine(Offset(court.left, court.top + court.height * 0.22), Offset(court.right, court.top + court.height * 0.22), line);
    canvas.drawLine(Offset(court.left, court.bottom - court.height * 0.22), Offset(court.right, court.bottom - court.height * 0.22), line);
  }

  void _tableTennis(Canvas canvas, Size size, Paint line) {
    final table = Rect.fromLTWH(size.width * 0.12, size.height * 0.28, size.width * 0.76, size.height * 0.44);
    canvas.drawRRect(RRect.fromRectAndRadius(table, const Radius.circular(4)), Paint()..color = const Color(0xFF1565C0));
    canvas.drawRect(table, line);
    canvas.drawLine(Offset(table.center.dx, table.top), Offset(table.center.dx, table.bottom), line..strokeWidth = 3);
    canvas.drawLine(Offset(table.left, table.center.dy), Offset(table.right, table.center.dy), line..strokeWidth = 1.4);
  }

  void _pool(Canvas canvas, Size size, Paint line, Paint fill) {
    final pool = Rect.fromLTWH(size.width * 0.06, size.height * 0.18, size.width * 0.88, size.height * 0.64);
    canvas.drawRRect(RRect.fromRectAndRadius(pool, const Radius.circular(10)), line);
    for (var i = 1; i < 8; i++) {
      final y = pool.top + pool.height * i / 8;
      canvas.drawLine(Offset(pool.left, y), Offset(pool.right, y), line..strokeWidth = 1);
    }
    canvas.drawCircle(Offset(pool.left + 16, pool.center.dy), 5, fill);
  }

  void _track(Canvas canvas, Size size, Paint line) {
    final oval = Rect.fromLTWH(size.width * 0.08, size.height * 0.12, size.width * 0.84, size.height * 0.76);
    canvas.drawOval(oval, line..strokeWidth = 10);
    canvas.drawOval(oval.deflate(18), line..strokeWidth = 2);
    canvas.drawRect(Rect.fromCenter(center: oval.center, width: oval.width * 0.42, height: oval.height * 0.38), Paint()..color = const Color(0xFF3D8B5F));
  }

  void _ring(Canvas canvas, Size size, Paint line, {required bool octagon}) {
    final box = Rect.fromLTWH(size.width * 0.18, size.height * 0.12, size.width * 0.64, size.height * 0.76);
    if (octagon) {
      final path = Path();
      final cx = box.center.dx;
      final cy = box.center.dy;
      final rx = box.width / 2;
      final ry = box.height / 2;
      for (var i = 0; i < 8; i++) {
        final a = (i * 45 - 22.5) * 3.14159 / 180;
        final p = Offset(cx + rx * 0.92 * (a.cosApprox), cy + ry * 0.92 * (a.sinApprox));
        if (i == 0) {
          path.moveTo(p.dx, p.dy);
        } else {
          path.lineTo(p.dx, p.dy);
        }
      }
      path.close();
      canvas.drawPath(path, Paint()..color = const Color(0xFF1ABC9C).withValues(alpha: 0.35));
      canvas.drawPath(path, line);
    } else {
      canvas.drawRRect(RRect.fromRectAndRadius(box, const Radius.circular(8)), Paint()..color = const Color(0xFF9B2226).withValues(alpha: 0.35));
      canvas.drawRRect(RRect.fromRectAndRadius(box, const Radius.circular(8)), line);
    }
  }

  void _diamond(Canvas canvas, Size size, Paint line, Paint fill) {
    final c = Offset(size.width / 2, size.height * 0.58);
    final d = size.shortestSide * 0.28;
    final path = Path()
      ..moveTo(c.dx, c.dy - d)
      ..lineTo(c.dx + d, c.dy)
      ..lineTo(c.dx, c.dy + d)
      ..lineTo(c.dx - d, c.dy)
      ..close();
    canvas.drawPath(path, Paint()..color = const Color(0xFFC4A574));
    canvas.drawPath(path, line);
    canvas.drawCircle(Offset(c.dx, c.dy - d), 5, fill);
    canvas.drawCircle(c, 4, fill);
  }

  void _loop(Canvas canvas, Size size, Paint line) {
    canvas.drawOval(Rect.fromLTWH(size.width * 0.1, size.height * 0.2, size.width * 0.8, size.height * 0.6), line..strokeWidth = 8);
    canvas.drawCircle(Offset(size.width * 0.22, size.height * 0.5), 10, Paint()..color = HubColors.orange);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

extension on double {
  double get cosApprox {
    // Avoid dart:math import issues in paint; use Flutter's dart:math
    return _cos(this);
  }

  double get sinApprox => _sin(this);
}

double _sin(double a) {
  return Offset.fromDirection(a).dy;
}

double _cos(double a) {
  return Offset.fromDirection(a).dx;
}

class IconFactGrid extends StatelessWidget {
  const IconFactGrid({super.key, required this.items});
  final List<(IconData, String, String)> items;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, c) {
        final cols = c.maxWidth > 700 ? 3 : (c.maxWidth > 420 ? 2 : 1);
        return GridView.count(
          crossAxisCount: cols,
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          crossAxisSpacing: 12,
          mainAxisSpacing: 12,
          childAspectRatio: 1.35,
          children: items
              .map(
                (e) => Container(
                  decoration: BoxDecoration(
                    color: const Color(0xFFF8FAFC),
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: const Color(0xFFE2E8F0)),
                  ),
                  padding: const EdgeInsets.all(14),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Icon(e.$1, color: HubColors.teal, size: 28),
                      const SizedBox(height: 8),
                      Text(e.$2, style: const TextStyle(fontWeight: FontWeight.w800)),
                      const SizedBox(height: 4),
                      Expanded(child: Text(e.$3, maxLines: 4, overflow: TextOverflow.ellipsis, style: const TextStyle(fontSize: 12, color: Color(0xFF475569), height: 1.3))),
                    ],
                  ),
                ),
              )
              .toList(),
        );
      },
    );
  }
}

class PositionBoard extends StatelessWidget {
  const PositionBoard({super.key, required this.slug, required this.names});
  final String slug;
  final List<String> names;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 240,
      child: Stack(
        children: [
          Positioned.fill(child: SportPitchDiagram(slug: slug)),
          ..._spots(names).asMap().entries.map((e) {
            return Align(
              alignment: e.value,
              child: Container(
                margin: const EdgeInsets.all(6),
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(color: HubColors.navy.withValues(alpha: 0.86), borderRadius: BorderRadius.circular(20)),
                child: Text(e.key < names.length ? names[e.key] : '', style: const TextStyle(color: Colors.white, fontSize: 10, fontWeight: FontWeight.w700)),
              ),
            );
          }),
        ],
      ),
    );
  }

  List<Alignment> _spots(List<String> names) {
    const presets = [
      Alignment(-0.75, 0),
      Alignment(-0.35, -0.55),
      Alignment(-0.35, 0.55),
      Alignment(0.15, -0.2),
      Alignment(0.15, 0.45),
      Alignment(0.72, 0),
      Alignment(0.45, -0.65),
      Alignment(0.45, 0.7),
    ];
    return List.generate(names.length.clamp(0, presets.length), (i) => presets[i]);
  }
}

IconData sectionIcon(String label) {
  switch (label) {
    case 'Overview':
      return Icons.sports;
    case 'History':
      return Icons.history_edu;
    case 'Rules':
      return Icons.gavel;
    case 'Players':
      return Icons.groups;
    case 'Positions':
      return Icons.grid_view;
    case 'Playing area':
      return Icons.map_outlined;
    case 'Equipment':
      return Icons.inventory_2_outlined;
    case 'Scoring':
      return Icons.scoreboard_outlined;
    case 'Fouls':
      return Icons.front_hand_outlined;
    case 'Training':
      return Icons.fitness_center;
    case 'Safety':
      return Icons.health_and_safety_outlined;
    case 'Terms':
      return Icons.menu_book_outlined;
    case 'FAQ':
      return Icons.help_outline;
    case 'Sources':
      return Icons.source_outlined;
    default:
      return Icons.info_outline;
  }
}
