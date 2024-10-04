import 'package:flutter/material.dart';
import 'package:flutter_application_1/components/address_list_tile.dart';
import 'package:flutter_application_1/components/floating_action_button.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: CustomFloatingActionButton(),
      body: Column(
        children: [
          // Image.asset(
          //   'assets/images/wheat.jpeg'
          // ),
          SizedBox(
            height: 150,
            child: ListView(
              children: const [
                AddressListTile(lat: "25.65", long: "43.5"),
                AddressListTile(lat: "25.65", long: "43.5"),
                AddressListTile(lat: "25.65", long: "43.5"),
                AddressListTile(lat: "25.65", long: "43.5"),
                AddressListTile(lat: "25.65", long: "43.5"),
              ],
            ),
          ),
        ],
      ),
    );

    // return
  }
}
