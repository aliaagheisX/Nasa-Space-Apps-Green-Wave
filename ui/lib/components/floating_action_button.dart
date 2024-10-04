import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:ui/components/custom_textfield.dart';
import 'package:ui/services/api.dart';
import 'package:dio/dio.dart';

class CustomFloatingActionButton extends StatelessWidget {
  CustomFloatingActionButton({super.key});

  final TextEditingController lat = TextEditingController();
  final TextEditingController long = TextEditingController();

  final Api api = Api(Dio());

  @override
  Widget build(BuildContext context) {
    return FloatingActionButton(
      onPressed: () async {
        Position position = await Geolocator.getCurrentPosition();
        log(position.toString());

        showDialog(
            context: context,
            builder: (BuildContext context) {
              return AlertDialog(
                title: const Text("Enter your location"),
                content: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    CustomTextField(
                      controller: lat,
                      name: 'lat',
                    ),
                    CustomTextField(
                      controller: long,
                      name: 'long',
                    ),
                  ],
                ),
                actions: [
                  TextButton(
                    onPressed: () {
                      api.post_data(lat.text, long.text);
                      Navigator.of(context).pop();
                    },
                    child: const Text("Save"),
                  ),
                  TextButton(
                    onPressed: () {
                      Navigator.of(context).pop();
                    },
                    child: const Text("Cancel"),
                  ),
                ],
              );
            });
      },
      backgroundColor: Colors.green,
      child: const Icon(Icons.add),
    );
  }
}
