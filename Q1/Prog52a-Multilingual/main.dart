import 'dart:io';

void main() {
  print('gimmie yo length or the baby gets it: ');
  int? len = int.parse(stdin.readLineSync()!);

  print('alr cool now how about that width: ');
  int? wid = int.parse(stdin.readLineSync()!);

  int area = len * wid;
  int perim = ((len * 2) + (wid * 2));

  print('your area is: ' + area.toString());
  print('your perimeter is: ' + perim.toString());
}
