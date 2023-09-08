#include <iostream>
using namespace std;

int main() {

  int len;

  int wid;
  
  cout << "enter yo length: ";

  cin >> len;

  cout << "";

  cout << "alr cool now enter yo width: ";

  cin >> wid;

  cout << "Your area is: " << (len * wid) << "\n";
  cout << "Your perimeter is: " << ((len*2) + (wid*2));
  
  return 0;
}
