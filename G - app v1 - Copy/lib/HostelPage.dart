import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:flutter_rating_bar/flutter_rating_bar.dart';
import 'dart:convert';

class HostelPage extends StatefulWidget {
  final String apiUrl;

  HostelPage({required this.apiUrl});

  @override
  _HostelPageState createState() => _HostelPageState();
}

class _HostelPageState extends State<HostelPage> {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController studentIdController = TextEditingController();
  final TextEditingController batchController = TextEditingController();
  final TextEditingController phoneNoController = TextEditingController();
  final TextEditingController grievanceController = TextEditingController();
  double importance = 0;

  Future<void> submitHostel(BuildContext context) async {
    if (nameController.text.isEmpty ||
        studentIdController.text.isEmpty ||
        batchController.text.isEmpty ||
        phoneNoController.text.isEmpty ||
        grievanceController.text.isEmpty) {
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: const Text('Submission Error'),
            content: const Text('Please fill all the fields.'),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text('OK'),
              ),
            ],
          );
        },
      );
      return;
    }

    final url = Uri.parse(widget.apiUrl);
    print({
      'student_name': nameController.text,
      'student_id': studentIdController.text,
      'batch': batchController.text,
      'phone_no': phoneNoController.text,
      'data': grievanceController.text,
      'importance': importance.toInt(),
    });

    final response = await http.post(
      url,
      body: jsonEncode({
        'student_name': nameController.text,
        'student_id': studentIdController.text,
        'batch': batchController.text,
        'phone_no': int.parse(phoneNoController.text),
        'data': grievanceController.text,
        'importance': importance.toInt(),
      }),
      headers: {"Content-Type": "application/json"},
    );

    print('Response status: ${response.statusCode}');
    print('Response body: ${response.body}');

    if (response.statusCode == 200) {
      nameController.clear();
      studentIdController.clear();
      batchController.clear();
      phoneNoController.clear();
      grievanceController.clear();
      importance = 0;

      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: const Text('Grievance Submission Status'),
            content: const Text('Grievance submitted successfully!'),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text('OK'),
              ),
            ],
          );
        },
      );
    } else {
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: const Text('Grievance Submission Status'),
            content: const Text('Failed to submit Grievance. Please try again.'),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text('OK'),
              ),
            ],
          );
        },
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Hostel Grievance Submission Page'),
        backgroundColor: Colors.deepPurple.shade900, // Change the app bar color here
      ),
      body: Stack(
        children: [
          Container(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Colors.deepPurple.shade900, // Deep purple color
                  Colors.deepPurple.shade900, // Purple color
                ],
              ),
            ),
          ),
          Center(
            child: Container(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  _buildTextField(nameController, 'Name', Icons.person),
                  _buildTextField(studentIdController, 'Student ID', Icons.confirmation_number),
                  _buildTextField(batchController, 'Batch', Icons.calendar_today),
                  _buildTextField(phoneNoController, 'Phone Number', Icons.phone),
                  _buildGrievanceField(),
                  const SizedBox(height: 20.0),
                  Text('Importance', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                  RatingBar.builder(
                    initialRating: importance,
                    minRating: 0,
                    direction: Axis.horizontal,
                    allowHalfRating: false,
                    itemCount: 5,
                    itemPadding: EdgeInsets.symmetric(horizontal: 4.0),
                    itemBuilder: (context, _) => Icon(
                      Icons.star,
                      color: Colors.amber,
                      size: 14,
                    ),
                    onRatingUpdate: (rating) {
                      setState(() {
                        importance = rating;
                      });
                    },
                  ),
                  const SizedBox(height: 40.0),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          submitHostel(context);
                        },
                        style: ElevatedButton.styleFrom(
                          primary: Colors.green,
                          shape: const CircleBorder(),
                          padding: const EdgeInsets.all(23.0),
                        ),
                        child: const Icon(Icons.send, size: 50),
                      ),
                      ElevatedButton(
                        onPressed: () {
                          Navigator.pop(context);
                        },
                        style: ElevatedButton.styleFrom(
                          primary: Colors.blue,
                          shape: const CircleBorder(),
                          padding: const EdgeInsets.all(23.0),
                        ),
                        child: const Icon(Icons.arrow_back, size: 50),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTextField(TextEditingController controller, String labelText, IconData icon) {
    return Card(
      elevation: 2.0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10.0),
      ),
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 10.0),
        child: TextFormField(
          controller: controller,
          decoration: InputDecoration(
            labelText: labelText,
            icon: Icon(icon),
            border: InputBorder.none,
          ),
        ),
      ),
    );
  }

  Widget _buildGrievanceField() {
    return Card(
      elevation: 2.0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10.0),
      ),
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 10.0),
        child: TextFormField(
          controller: grievanceController,
          maxLines: 3,
          decoration: const InputDecoration(
            labelText: 'Grievance',
            icon: Icon(Icons.feedback),
            border: InputBorder.none,
          ),
        ),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: HostelPage(apiUrl: 'http://192.168.43.192:8000/hostel/data/'),
  ));
}
