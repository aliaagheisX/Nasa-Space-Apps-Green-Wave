import 'package:dio/dio.dart';

class Api {
  final Dio dio;
  Api(this.dio);

  final String baseurl = 'http://10.0.2.2:5000/';

  Future<List<dynamic>> get_data() async {
    final Map<String, String> data = {'username': 'menna'};
    try {
      Response response = await dio.post(
        '${baseurl}getMessage',
        data: data,
        options: Options(
          followRedirects: false,
          validateStatus: (status) => true,
        ),
      );
      return response.data['messages'];
    } catch (e) {
      return [e.toString()];
    }
  }

  Future<String?> post_data(String lat, String long) async {
    final Map<String, String> data = {'lat': lat, 'long': long};
    try {
      Response response = await dio.post(
        '${baseurl}fertilizers',
        data: data,
        options: Options(
          followRedirects: false,
          validateStatus: (status) => true,
        ),
      );
      return response.data['message'];
    } catch (e) {
      return e.toString();
    }
  }

  Future<String?> patch_data(String lat, String long) async {
    final Map<String, String> data = {'lat': lat, 'long': long};
    try {
      Response response = await dio.patch(
        baseurl,
        data: data,
        options: Options(
          followRedirects: false,
          validateStatus: (status) => true,
        ),
      );
      return response.data['message'];
    } catch (e) {
      return e.toString();
    }
  }
}
