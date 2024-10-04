import 'dart:developer';
import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'package:flutter_application_1/components/custom_textfield.dart';
import 'package:flutter_application_1/services/api.dart';
import 'package:flutter_sms/flutter_sms.dart';
import 'package:geolocator/geolocator.dart';
import 'package:geocoding/geocoding.dart';

class CustomFloatingActionButton extends StatelessWidget {
  CustomFloatingActionButton({super.key});

  final TextEditingController lat = TextEditingController();
  final TextEditingController long = TextEditingController();

  final Api api = Api(Dio());

  @override
  Widget build(BuildContext context) {
    return FloatingActionButton(
      onPressed: () async {
        // LocationPermission permission = await Geolocator.requestPermission();

        // Position position = await Geolocator.getCurrentPosition();
        // log(position.toString());

        // List<Placemark> placemarks = await placemarkFromCoordinates(
        //     position.latitude, position.longitude);
        // Placemark place = placemarks[0];
        // log("El place gaai : ");
        // log(place.toString());

        String _result = await sendSMS(message: "Hello msg", recipients: [""])
            .catchError((onError) {
          print(onError);
        });
        print(_result);

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
