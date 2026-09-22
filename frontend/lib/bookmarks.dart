import 'package:shared_preferences/shared_preferences.dart';

class BookmarkStore {
  static const _key = 'sports_hub_bookmarks';

  Future<List<String>> slugs() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getStringList(_key) ?? [];
  }

  Future<bool> isSaved(String slug) async {
    return (await slugs()).contains(slug);
  }

  Future<void> toggle(String slug) async {
    final prefs = await SharedPreferences.getInstance();
    final current = List<String>.from(prefs.getStringList(_key) ?? <String>[]);
    if (current.contains(slug)) {
      current.remove(slug);
    } else {
      current.add(slug);
    }
    await prefs.setStringList(_key, current);
  }
}

final bookmarks = BookmarkStore();
