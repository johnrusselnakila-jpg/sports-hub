class CategoryItem {
  CategoryItem({
    required this.id,
    required this.slug,
    required this.name,
    required this.description,
    this.icon,
    this.sportCount,
  });

  final int id;
  final String slug;
  final String name;
  final String description;
  final String? icon;
  final int? sportCount;

  factory CategoryItem.fromJson(Map<String, dynamic> json) => CategoryItem(
        id: json['id'] as int,
        slug: json['slug'] as String,
        name: json['name'] as String,
        description: json['description'] as String? ?? '',
        icon: json['icon'] as String?,
        sportCount: json['sport_count'] as int?,
      );
}

class SportSummary {
  SportSummary({
    required this.id,
    required this.slug,
    required this.name,
    required this.tagline,
    required this.overview,
    required this.featured,
    required this.popular,
    required this.governingOrg,
    this.icon,
    this.accentColor,
    this.categories = const [],
    this.updatedAt,
  });

  final int id;
  final String slug;
  final String name;
  final String tagline;
  final String overview;
  final bool featured;
  final bool popular;
  final String governingOrg;
  final String? icon;
  final String? accentColor;
  final List<CategoryItem> categories;
  final String? updatedAt;

  factory SportSummary.fromJson(Map<String, dynamic> json) => SportSummary(
        id: json['id'] as int,
        slug: json['slug'] as String,
        name: json['name'] as String,
        tagline: json['tagline'] as String? ?? '',
        overview: json['overview'] as String? ?? '',
        featured: json['featured'] == true,
        popular: json['popular'] == true,
        governingOrg: json['governing_org'] as String? ?? '',
        icon: json['icon'] as String?,
        accentColor: json['accent_color'] as String?,
        categories: (json['categories'] as List? ?? [])
            .map((e) => CategoryItem.fromJson(Map<String, dynamic>.from(e as Map)))
            .toList(),
        updatedAt: json['updated_at'] as String?,
      );
}

class RuleItem {
  RuleItem.fromJson(Map<String, dynamic> json)
      : id = json['id'] as int,
        title = json['title'] as String,
        content = json['content'] as String,
        contentType = json['content_type'] as String? ?? 'educational',
        sourceOrg = json['source_org'] as String?,
        ruleEdition = json['rule_edition'] as String?,
        sportName = json['sport_name'] as String?,
        sportSlug = json['sport_slug'] as String?;

  final int id;
  final String title;
  final String content;
  final String contentType;
  final String? sourceOrg;
  final String? ruleEdition;
  final String? sportName;
  final String? sportSlug;
}

class EquipmentItem {
  EquipmentItem.fromJson(Map<String, dynamic> json)
      : id = json['id'] as int,
        name = json['name'] as String,
        purpose = json['purpose'] as String,
        specifications = json['specifications'] as String?,
        safety = json['safety_considerations'] as String?;

  final int id;
  final String name;
  final String purpose;
  final String? specifications;
  final String? safety;
}

class TechniqueItem {
  TechniqueItem.fromJson(Map<String, dynamic> json)
      : id = json['id'] as int,
        name = json['name'] as String,
        description = json['description'] as String,
        steps = (json['steps'] as List? ?? []).map((e) => e.toString()).toList(),
        beginnerTips = json['beginner_tips'] as String?,
        commonMistakes = json['common_mistakes'] as String?,
        safetyReminders = json['safety_reminders'] as String?;

  final int id;
  final String name;
  final String description;
  final List<String> steps;
  final String? beginnerTips;
  final String? commonMistakes;
  final String? safetyReminders;
}

class NamedText {
  NamedText({required this.name, required this.description, this.kind});
  final String name;
  final String description;
  final String? kind;
  factory NamedText.fromJson(Map<String, dynamic> json, {String nameKey = 'name', String descKey = 'description'}) =>
      NamedText(
        name: json[nameKey] as String? ?? json['term'] as String? ?? json['title'] as String? ?? '',
        description: json[descKey] as String? ?? json['definition'] as String? ?? json['content'] as String? ?? json['answer'] as String? ?? '',
        kind: json['kind'] as String? ?? json['content_type'] as String? ?? json['topic'] as String?,
      );
}

class SearchHit {
  SearchHit.fromJson(Map<String, dynamic> json)
      : type = json['type'] as String? ?? '',
        title = json['title'] as String? ?? '',
        snippet = json['snippet'] as String? ?? '',
        sportSlug = json['sport_slug'] as String?,
        sportName = json['sport_name'] as String?;

  final String type;
  final String title;
  final String snippet;
  final String? sportSlug;
  final String? sportName;
}

class SportDetail {
  SportDetail.fromJson(Map<String, dynamic> json)
      : summary = SportSummary.fromJson(json),
        overview = json['overview'] as String? ?? '',
        history = json['history'] as String? ?? '',
        playerCount = json['player_count'] as String? ?? '',
        courtDimensions = json['court_dimensions'] as String? ?? '',
        scoringSystem = json['scoring_system'] as String? ?? '',
        rules = (json['rules'] as List? ?? []).map((e) => RuleItem.fromJson(Map<String, dynamic>.from(e as Map))).toList(),
        equipment = (json['equipment'] as List? ?? []).map((e) => EquipmentItem.fromJson(Map<String, dynamic>.from(e as Map))).toList(),
        techniques = (json['techniques'] as List? ?? []).map((e) => TechniqueItem.fromJson(Map<String, dynamic>.from(e as Map))).toList(),
        safety = (json['safety_guidelines'] as List? ?? []).map((e) => NamedText.fromJson(Map<String, dynamic>.from(e as Map), nameKey: 'title', descKey: 'content')).toList(),
        terminology = (json['terminology'] as List? ?? []).map((e) => NamedText.fromJson(Map<String, dynamic>.from(e as Map))).toList(),
        faqs = (json['faqs'] as List? ?? []).map((e) => NamedText.fromJson(Map<String, dynamic>.from(e as Map), nameKey: 'question', descKey: 'answer')).toList(),
        references = (json['references'] as List? ?? []).map((e) => Map<String, dynamic>.from(e as Map)).toList(),
        positions = (json['positions'] as List? ?? []).map((e) => NamedText.fromJson(Map<String, dynamic>.from(e as Map))).toList(),
        fouls = (json['fouls_violations'] as List? ?? []).map((e) => NamedText.fromJson(Map<String, dynamic>.from(e as Map))).toList();

  final SportSummary summary;
  final String overview;
  final String history;
  final String playerCount;
  final String courtDimensions;
  final String scoringSystem;
  final List<RuleItem> rules;
  final List<EquipmentItem> equipment;
  final List<TechniqueItem> techniques;
  final List<NamedText> safety;
  final List<NamedText> terminology;
  final List<NamedText> faqs;
  final List<Map<String, dynamic>> references;
  final List<NamedText> positions;
  final List<NamedText> fouls;
}
