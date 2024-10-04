import 'package:flutter/material.dart';

class AddressListTile extends StatelessWidget {
  const AddressListTile({super.key, required this.lat, required this.long});

  final String lat;
  final String long;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 5.0),
      child: ListTile(
        shape: const OutlineInputBorder(
            borderRadius: BorderRadius.all(Radius.circular(5))),
        title: Text("Lat : $lat, Long : $long"),
        enabled: true,
      ),
    );
  }
}
