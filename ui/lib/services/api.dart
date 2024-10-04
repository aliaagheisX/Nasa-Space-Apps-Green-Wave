import 'package:dio/dio.dart';

class Api {
  final Dio dio;
  Api(this.dio);

  final String url = 'yara';

  Future<dynamic>? get_data() {}

  Future<String?> post_data(String lat, String long) async {
    final Map<String, String> data = {'lat': lat, 'long': long};
    try {
      await dio.post(url, data: data);
      return null;
    } catch (e) {
      return e.toString();
    }
  }
}
