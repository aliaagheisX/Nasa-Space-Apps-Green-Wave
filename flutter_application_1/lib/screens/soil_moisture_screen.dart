import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';

class AnimatedMoistureGauge extends StatefulWidget {
  const AnimatedMoistureGauge({super.key});

  @override
  _AnimatedMoistureGaugeState createState() => _AnimatedMoistureGaugeState();
}

class _AnimatedMoistureGaugeState extends State<AnimatedMoistureGauge>
    with SingleTickerProviderStateMixin {
  late AnimationController _animationController;
  late Animation<double> _animation;
  double _currentValue = 0; // Current value of the gauge
  double _targetValue = 0; // Value set by the slider

  @override
  void initState() {
    super.initState();

    // Initialize the animation controller
    _animationController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 2), // Duration of the animation
    );

    // Initialize the animation with a dummy value
    _animation = Tween<double>(begin: 0, end: 0).animate(_animationController)
      ..addListener(() {
        setState(() {
          _currentValue = _animation.value;
        });
      });
    _animateGauge(30);
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }

  void _animateGauge(double newValue) {
    // Stop the previous animation and reset controller
    _animationController.stop();
    _animationController.reset();

    // Update the animation to go from the current value to the new value
    _animation = Tween<double>(begin: _currentValue, end: newValue)
        .animate(_animationController)
      ..addListener(() {
        setState(() {
          _currentValue = _animation.value;
        });
      });

    // Start the new animation
    _animationController.forward();
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text(
            'نسبة رطوبة التربة',
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 20),
          const Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text('اقل من المتوسط',
                  style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.red)),
              Text('متوسط',
                  style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.green)),
              Text('اعلى من المتوسط',
                  style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.red)),
            ],
          ),
          const SizedBox(height: 10),
          // Display the gauge
          SfRadialGauge(
            axes: <RadialAxis>[
              RadialAxis(
                showTicks: false,
                showLabels: false,
                minimum: 0,
                maximum: 100,
                ranges: <GaugeRange>[
                  GaugeRange(
                    startValue: 0,
                    endValue: 33,
                    color: Colors.red, // Low moisture
                  ),
                  GaugeRange(
                    startValue: 34,
                    endValue: 66,
                    color: Colors.green, // Medium moisture
                  ),
                  GaugeRange(
                    startValue: 67,
                    endValue: 100,
                    color: Colors.red, // High moisture
                  ),
                ],
                pointers: <GaugePointer>[
                  NeedlePointer(
                    value: _currentValue,
                  ),
                  // Animated value
                ],
                annotations: <GaugeAnnotation>[
                  GaugeAnnotation(
                    widget: Text(
                      _currentValue.toStringAsFixed(1),
                      style:
                          const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                    ),
                    angle: 90,
                    positionFactor: 0.5,
                  ),
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }
}
