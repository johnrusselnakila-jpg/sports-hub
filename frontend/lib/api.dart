import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import 'config.dart';
import 'models.dart';

class ApiException implements Exception {
  ApiException(this.message);
  final String message;
  @override
  String toString() => message;
}

class Api {
  static const _tokenKey = 'sports_hub_token';

  Future<Map<String, String>> _headers({bool auth = false}) async {
    final headers = {'Content-Type': 'application/json', 'Accept': 'application/json'};
    if (auth) {
      final prefs = await SharedPreferences.getInstance();
      final token = prefs.getString(_tokenKey);
      if (token != null) headers['Authorization'] = 'Bearer $token';
    }
    return headers;
  }

  Uri _uri(String path, [Map<String, String>? query]) {
    return Uri.parse('${ApiConfig.baseUrl}$path').replace(queryParameters: query);
  }

  Future<dynamic> _get(String path, {Map<String, String>? query, bool auth = false}) async {
    final response = await http.get(_uri(path, query), headers: await _headers(auth: auth));
    return _decode(response);
  }

  Future<dynamic> _send(String method, String path, {Map<String, dynamic>? body, bool auth = true}) async {
    final uri = _uri(path);
    final headers = await _headers(auth: auth);
    final encoded = jsonEncode(body ?? {});
    late http.Response response;
    switch (method) {
      case 'POST':
        response = await http.post(uri, headers: headers, body: encoded);
        break;
      case 'PUT':
        response = await http.put(uri, headers: headers, body: encoded);
        break;
      case 'DELETE':
        response = await http.delete(uri, headers: headers);
        break;
      default:
        throw ApiException('Unsupported method');
    }
    return _decode(response);
  }

  dynamic _decode(http.Response response) {
    final body = response.body.isEmpty ? {} : jsonDecode(response.body);
    if (response.statusCode >= 400) {
      final message = body is Map ? (body['error'] ?? 'Request failed') : 'Request failed';
      throw ApiException(message.toString());
    }
    return body;
  }

  Future<List<SportSummary>> sports({String? category, bool featured = false, bool popular = false}) async {
    final query = <String, String>{};
    if (category != null) query['category'] = category;
    if (featured) query['featured'] = 'true';
    if (popular) query['popular'] = 'true';
    final data = await _get('/api/sports', query: query.isEmpty ? null : query);
    return (data['sports'] as List).map((e) => SportSummary.fromJson(Map<String, dynamic>.from(e as Map))).toList();
  }

  Future<SportDetail> sport(String slug) async {
    final data = await _get('/api/sports/$slug');
    return SportDetail.fromJson(Map<String, dynamic>.from(data as Map));
  }

  Future<List<CategoryItem>> categories() async {
    final data = await _get('/api/categories');
    return (data['categories'] as List).map((e) => CategoryItem.fromJson(Map<String, dynamic>.from(e as Map))).toList();
  }

  Future<List<SportSummary>> categorySports(String slug) async {
    final data = await _get('/api/categories/$slug/sports');
    return (data['sports'] as List).map((e) => SportSummary.fromJson(Map<String, dynamic>.from(e as Map))).toList();
  }

  Future<Map<String, dynamic>> search(String q) async {
    return Map<String, dynamic>.from(await _get('/api/search', query: {'q': q}) as Map);
  }

  Future<Map<String, dynamic>> safety({String? sport}) async {
    return Map<String, dynamic>.from(
      await _get('/api/safety', query: sport == null ? null : {'sport': sport}) as Map,
    );
  }

  Future<Map<String, dynamic>> about() async {
    return Map<String, dynamic>.from(await _get('/api/site/about') as Map);
  }

  Future<Map<String, dynamic>> login(String email, String password) async {
    final data = await _send('POST', '/api/auth/login', body: {'email': email, 'password': password}, auth: false);
    final token = data['access_token'] as String;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_tokenKey, token);
    return Map<String, dynamic>.from(data['user'] as Map);
  }

  Future<void> logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_tokenKey);
  }

  Future<Map<String, dynamic>?> me() async {
    final prefs = await SharedPreferences.getInstance();
    if (prefs.getString(_tokenKey) == null) return null;
    try {
      final data = await _get('/api/auth/me', auth: true);
      return Map<String, dynamic>.from(data['user'] as Map);
    } catch (_) {
      return null;
    }
  }

  Future<dynamic> adminPost(String path, Map<String, dynamic> body) => _send('POST', path, body: body);
  Future<dynamic> adminPut(String path, Map<String, dynamic> body) => _send('PUT', path, body: body);
  Future<dynamic> adminDelete(String path) => _send('DELETE', path);
}

final api = Api();
