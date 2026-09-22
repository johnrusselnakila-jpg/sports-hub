import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class HubColors {
  static const navy = Color(0xFF0B1F3A);
  static const navyDeep = Color(0xFF07111F);
  static const teal = Color(0xFF2A9D8F);
  static const orange = Color(0xFFE85D04);
  static const sand = Color(0xFFF4F1EA);
  static const ink = Color(0xFF12233A);
}

ThemeData buildTheme() {
  final base = ThemeData(
    useMaterial3: true,
    colorScheme: ColorScheme.fromSeed(
      seedColor: HubColors.navy,
      primary: HubColors.navy,
      secondary: HubColors.teal,
      brightness: Brightness.light,
    ),
  );
  return base.copyWith(
    textTheme: GoogleFonts.outfitTextTheme(base.textTheme),
    scaffoldBackgroundColor: HubColors.sand,
    appBarTheme: AppBarTheme(
      backgroundColor: HubColors.navy,
      foregroundColor: Colors.white,
      elevation: 0,
      titleTextStyle: GoogleFonts.outfit(
        fontWeight: FontWeight.w700,
        fontSize: 20,
        color: Colors.white,
      ),
    ),
    cardTheme: CardThemeData(
      elevation: 0,
      color: Colors.white,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
      margin: EdgeInsets.zero,
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: Colors.white,
      border: OutlineInputBorder(borderRadius: BorderRadius.circular(14)),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(14),
        borderSide: const BorderSide(color: Color(0xDDE2E8F0)),
      ),
    ),
  );
}
