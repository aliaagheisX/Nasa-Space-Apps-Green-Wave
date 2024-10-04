import 'package:flutter/material.dart';
import 'package:flutter_application_1/screens/home.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:geocoding/geocoding.dart';


class NewHome extends StatelessWidget {
  const NewHome({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        image: DecorationImage(
            image: AssetImage('assets/images/image.png'),
            fit: BoxFit.cover,
            opacity: 0.5),
      ),
      child: Directionality(
        textDirection: TextDirection.rtl, // Set global RTL text direction
        child: SimpleDialog(
          elevation: 25,
          shape: RoundedRectangleBorder(
            borderRadius:
                BorderRadius.circular(8), // Set your desired border radius here
          ),
          backgroundColor: const Color.fromARGB(255, 74, 189, 78),
          title: const Text(
            'هل تود استخدام أخر موقع تم تسجيله الموقع الحالي؟',
            style: TextStyle(fontSize: 20),
          ),
          children: <Widget>[
            Container(
              padding: EdgeInsets.zero,
              margin: EdgeInsets.symmetric(horizontal: 10),
              color: const Color.fromARGB(255, 240, 225, 89),
              child: SimpleDialogOption(
                padding: EdgeInsets.symmetric(vertical: 5, horizontal: 3),
                onPressed: () {},
                child: const Text(
                  '📍استخدم الموقع المسجل',
                  style: TextStyle(
                      fontStyle: FontStyle.italic, fontWeight: FontWeight.bold),
                ),
              ),
            ),
            Container(
              margin: EdgeInsets.symmetric(horizontal: 10, vertical: 5),
              color: const Color.fromARGB(255, 213, 227, 15),
              child: SimpleDialogOption(
                padding: EdgeInsets.symmetric(vertical: 5, horizontal: 3),
                onPressed: () {
                  Navigator.of(context).push(
                      MaterialPageRoute(builder: (context) => HomeScreen()));
                },
                child: const Text(
                  '🗺️ استخدم الموقع الحالي',
                  style: TextStyle(
                      fontStyle: FontStyle.italic, fontWeight: FontWeight.bold),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
