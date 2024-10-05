import 'dart:developer';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:flutter_application_1/components/custom_card.dart';
import 'package:flutter_application_1/screens/soil_moisture_screen.dart';
import 'package:flutter_application_1/services/api.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:geolocator/geolocator.dart';

class MyHomePage extends StatelessWidget {
  MyHomePage({super.key});

  final Api api = Api(Dio());
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          actions: [
            IconButton(
              icon: const Icon(Icons.location_on),
              onPressed: () async {
                print('Settings button pressed!');
                LocationPermission permission =
                    await Geolocator.checkPermission();
                if (permission == LocationPermission.denied) {
                  permission = await Geolocator.requestPermission();
                }
                if (permission != LocationPermission.denied) {
                  Position position = await Geolocator.getCurrentPosition();
                  log(position.toString());
                  String? s = await api.patch_data(position.altitude.toString(),
                      position.longitude.toString());
                  await showDialog(
                      context: context,
                      builder: (context) {
                        Future.delayed(const Duration(seconds: 2), () {
                          Navigator.of(context).pop(true);
                        });
                        return const AlertDialog(
                          content: Column(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Text("تم تغيير موقعك بنجاح",
                                  style: TextStyle(
                                    fontSize: 20,
                                  )),
                              SizedBox(
                                height: 20,
                              ),
                              Icon(
                                Icons.check_circle,
                                color: Colors.green,
                                size: 60,
                              ),
                            ],
                          ),
                        );
                      });
                }
              },
            ),
          ],
          title: const Text("Green Wave"),
          leading: const Icon(FontAwesomeIcons.sunPlantWilt),
          elevation: 10,
          // shadowColor: Colors.green,
          backgroundColor: Color.fromARGB(255, 33, 193, 39),
        ),
        body:  TabBarView(
          children: [
            const AnimatedMoistureGauge(),
            Customcard(
              title: "",
              body: "",
            ),
          ],
        ),
        bottomNavigationBar: const BottomAppBar(
          child: TabBar(
            tabs: [
              Tab(icon: Icon(Icons.grain), text: "رطوبة التربة"),
              Tab(icon: Icon(Icons.nature), text: "صحة النبات"),
            ],
            labelColor: Colors.blue,
            unselectedLabelColor: Colors.grey,
            indicatorColor: Colors.blue,
          ),
        ),
      ),
    );
  }
}
