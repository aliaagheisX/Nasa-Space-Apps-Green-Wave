import 'package:flutter/material.dart';
// import 'package:flutter_application_1/components/address_list_tile.dart';
import 'package:flutter_application_1/components/floating_action_button.dart';
import 'package:geocoding/geocoding.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  Future<String?> getAddressName(double longitide, double latitude) async {
    List<Placemark> placemarks =
        await placemarkFromCoordinates(37.4219983, -122.084);
    Placemark place = placemarks[0];
    // log("El place gaai : ");
    // log(place.toString());
    return place.subAdministrativeArea;
  }

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
                // AddressListTile(lat: "25.65", long: "43.5"),
                // AddressListTile(lat: "25.65", long: "43.5"),
                // AddressListTile(lat: "25.65", long: "43.5"),
                // AddressListTile(lat: "25.65", long: "43.5"),
                // AddressListTile(lat: "25.65", long: "43.5"),
              ],
            ),
          ),
        ],
      ),
    );

    // return
  }
}
