import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:flutter_application_1/components/customListView.dart';
import 'package:flutter_application_1/services/api.dart';

class Customcard extends StatelessWidget {
  Customcard({super.key, required this.title, required this.body});
  final String title;
  final String body;

  final Api api = Api(Dio());

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: api.get_data(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Center(
              child: CircularProgressIndicator(
            color: Colors.green,
          ));
        } else if (snapshot.hasError) {
          return Text('Error: ${snapshot.error}');
        } else if (snapshot.hasData) {
          final data = snapshot.data as List<dynamic>;

          return ListView.builder(
              itemCount: data.length,
              itemBuilder: (context, index) {
                return CustomListView(
                    title: data[index]['message'], body: data[index]['time']);
              });
        } else {
          return const Center(
              child: CircularProgressIndicator(
            color: Colors.green,
          ));
        }
      },
    );
  }
}
