import 'dart:developer';

import 'package:another_flutter_splash_screen/another_flutter_splash_screen.dart';
import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:flutter_application_1/screens/tabbar_screen.dart';
import 'package:flutter_application_1/services/api.dart';
import 'package:geolocator/geolocator.dart';

class SplashScreen extends StatelessWidget {
  SplashScreen({super.key});
  final Api api = Api(Dio());
  @override
  Widget build(BuildContext context) {
    return FlutterSplashScreen.fadeIn(
      // gradient: LinearGradient(colors: [
      //   const Color.fromARGB(255, 74, 189, 78),
      //   const Color.fromARGB(255, 138, 183, 138),
      // ], end: Alignment.bottomRight, begin: Alignment.topLeft),
      backgroundColor: const Color.fromRGBO(255, 255, 255, 1),
      onInit: () async {
        LocationPermission permission = await Geolocator.checkPermission();
        if (permission == LocationPermission.denied) {
          permission = await Geolocator.requestPermission();
        }
        if (permission != LocationPermission.denied) {
          Position position = await Geolocator.getCurrentPosition();
          log(position.toString());
          String? s = await api.post_data(
              position.altitude.toString(), position.longitude.toString());
        }
        debugPrint("On Init");
      },
      onEnd: () {
        debugPrint("On End");
      },
      childWidget: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          SizedBox(
            // height: 00,
            // width: 300,
            child: Image.asset("assets/farmer.gif"),
          ),
          const Text(
            "GreenWave",
            style: TextStyle(
              color: Color.fromARGB(255, 33, 193, 39),
              fontSize: 30,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
      onAnimationEnd: () => debugPrint("On Fade In End"),
      nextScreen: MyHomePage(),
    );
  }
}
