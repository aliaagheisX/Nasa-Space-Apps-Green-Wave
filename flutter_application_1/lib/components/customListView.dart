import 'package:flutter/material.dart';

class CustomListView extends StatelessWidget {
  const CustomListView({super.key, required this.title, required this.body});
  final String title;
  final String body;
  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 3, vertical: 5),
      decoration: BoxDecoration(
        boxShadow: const [
          BoxShadow(
              color: Color.fromARGB(255, 45, 45, 45),
              spreadRadius: 0.3, // How far the shadow spreads
              blurRadius: 4, // How soft the shadow is
              offset: const Offset(2, 2))
        ],
        color: const Color(0xFFFFFCF7), // background color
        border: Border.all(
          color: Colors.transparent, // Border color
          width: 2.0, // Border width
        ),
        borderRadius:
            BorderRadius.circular(15.0), // Optional for rounded corners
      ),
      child: ListTile(
        // selectedColor: Colors.grey,
        title: Directionality(
          textDirection: TextDirection.rtl,
          child: Text(title,
              style: const TextStyle(
                  fontSize: 18,
                  color: Colors.black,
                  fontWeight: FontWeight.bold)),
        ),
        subtitle: Text(
          body,
          style: const TextStyle(
              fontSize: 15,
              color: Color.fromARGB(255, 124, 122, 122),
              fontWeight: FontWeight.bold),
        ),
      ),
    );
  }
}
