import 'package:flutter/material.dart';

class CustomTextField extends StatelessWidget {
  const CustomTextField({
    super.key,
    required this.controller,
    required this.name,

  });

  final TextEditingController controller;
  final String name;

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: controller,
      decoration: InputDecoration(
          border: const OutlineInputBorder(
            borderSide: BorderSide(
              color: Colors.green,
            ),
            borderRadius: BorderRadius.all(Radius.circular(5)),
          ),
          hintText: name),
    );
  }
}
