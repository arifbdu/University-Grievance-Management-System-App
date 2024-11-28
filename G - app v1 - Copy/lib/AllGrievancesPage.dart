import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class GrievanceType {
  final String title;
  final String apiUrl;

  GrievanceType({required this.title, required this.apiUrl});
}

class AllGrievancesPage extends StatefulWidget {
  @override
  _AllGrievancesPageState createState() => _AllGrievancesPageState();
}

class _AllGrievancesPageState extends State<AllGrievancesPage> {
  List<GrievanceType> grievanceTypes = [
    GrievanceType(
        title: 'Hostel', apiUrl: 'http://192.168.43.192:8000/hostel/data/'),
    GrievanceType(
        title: 'Admin', apiUrl: 'http://192.168.43.192:8000/authority/data/'),
    GrievanceType(
        title: 'Food', apiUrl: 'http://192.168.43.192:8000/food/data/'),
    GrievanceType(
        title: 'Certificate',
        apiUrl: 'http://192.168.43.192:8000/certificate/data/'),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('All Grievances'),
        backgroundColor: Colors.deepPurple[900],
      ),
      body: Container(
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
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const SizedBox(height: 30),
            const Text(
              'Choose Grievance Type',
              style: TextStyle(
                fontSize: 25,
                fontWeight: FontWeight.bold,
                  color: Colors.white
              ),
            ),
            const SizedBox(height: 30),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Column(
                  children: [
                    CircularButton(
                      color: Colors.red,
                      title: grievanceTypes[0].title,
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => GrievanceListPage(
                              apiUrl: grievanceTypes[0].apiUrl,
                            ),
                          ),
                        );
                      },
                    ),
                    const SizedBox(height: 10),
                    CircularButton(
                      color: Colors.green,
                      title: grievanceTypes[2].title,
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => GrievanceListPage(
                              apiUrl: grievanceTypes[2].apiUrl,
                            ),
                          ),
                        );
                      },
                    ),
                  ],
                ),
                const SizedBox(width: 20),
                Column(
                  children: [
                    CircularButton(
                      color: Colors.blue,
                      title: grievanceTypes[1].title,
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => GrievanceListPage(
                              apiUrl: grievanceTypes[1].apiUrl,
                            ),
                          ),
                        );
                      },
                    ),
                    const SizedBox(height: 10),
                    CircularButton(
                      color: Colors.orange,
                      title: grievanceTypes[3].title,
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => GrievanceListPage(
                              apiUrl: grievanceTypes[3].apiUrl,
                            ),
                          ),
                        );
                      },
                    ),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class GrievanceListPage extends StatefulWidget {
  final String apiUrl;

  GrievanceListPage({required this.apiUrl});

  @override
  _GrievanceListPageState createState() => _GrievanceListPageState();
}

class _GrievanceListPageState extends State<GrievanceListPage> {
  List<Map<String, dynamic>> grievances = [];

  @override
  void initState() {
    super.initState();
    fetchData(widget.apiUrl);
  }

  Future<void> fetchData(String apiUrl) async {
    final response = await http.get(Uri.parse(apiUrl));
    if (response.statusCode == 200) {
      setState(() {
        List<Map<String, dynamic>> fetchedData =
        List<Map<String, dynamic>>.from(json.decode(response.body));
        grievances.addAll(fetchedData);
        grievances.sort((a, b) => b['importance'].compareTo(a['importance']));
      });
    } else {
      print('Failed to fetch data from $apiUrl');
    }
  }

  Widget buildImportanceStars(int importance) {
    List<Widget> stars = [];
    for (int i = 0; i < importance; i++) {
      stars.add(const Icon(Icons.star, color: Colors.amber));
    }
    return Row(children: stars);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Grievances'),
        backgroundColor: Colors.deepPurple[900],
      ),
      body: Container(
        decoration:BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              Colors.deepPurple.shade900, // Deep purple color
              Colors.deepPurple.shade900, // Purple color
            ],
          ),
        ),
        child: grievances.isNotEmpty
            ? ListView.builder(
          itemCount: grievances.length,
          itemBuilder: (context, index) {
            final grievance = grievances[index];
            return Card(
              color: grievance['status'] == 1
                  ? Colors.blue
                  : Colors.redAccent[400],
              elevation: 3,
              margin: const EdgeInsets.symmetric(
                  horizontal: 10, vertical: 5),
              child: ListTile(
                title: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Name: ${grievance['student_name']}',
                      style: const TextStyle(
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    SizedBox(height: 5),
                    Text(
                      'Student ID: ${grievance['student_id']}',
                      style: TextStyle(
                          color: Colors.white.withOpacity(0.8)),
                    ),
                    Text(
                      'Batch: ${grievance['batch']}',
                      style: TextStyle(
                          color: Colors.white.withOpacity(0.8)),
                    ),
                    Text(
                      'Phone Number: ${grievance['phone_no']}',
                      style: TextStyle(
                          color: Colors.white.withOpacity(0.8)),
                    ),
                  ],
                ),
                subtitle: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    SizedBox(height: 10),
                    Text(
                      'Problem:',
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 16,
                      ),
                    ),
                    SizedBox(height: 5),
                    Row(
                      children: [
                        Expanded(
                          child: Text(
                            '${grievance['data']}',
                            style: TextStyle(color: Colors.white),
                          ),
                        ),
                      ],
                    ),
                    SizedBox(height: 10),
                    Row(
                      children: [
                        Text(
                          'Importance: ',
                          style: TextStyle(
                            color: Colors.white,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        buildImportanceStars(
                            grievance['importance']),
                      ],
                    ),
                  ],
                ),
                trailing: Text(
                  grievance['status'] == 0
                      ? 'Submitted'
                      : 'Solved',
                  style: TextStyle(
                    color: grievance['status'] == 0
                        ? Colors.white
                        : Colors.white,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            );
          },
        )
            : const Center(
          child: CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
          ),
        ),
      ),
    );
  }
}

class CircularButton extends StatelessWidget {
  final Color color;
  final String title;
  final Function onTap;

  CircularButton(
      {required this.color, required this.title, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => onTap(),
      child: Container(
        width: 120,
        height: 120,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: color,
        ),
        child: Center(
          child: Text(
            title,
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: AllGrievancesPage(),
  ));
}
