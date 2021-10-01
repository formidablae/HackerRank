#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string first;
    string second;

    cin >> first;
    cin >> second;

    cout << first.size() << " " << second.size() << "\n";

    cout << first << second << "\n";

    cout << second[0] << first.substr(1, first.size()) << " " << first[0] << second.substr(1, second.size());
  
    return 0;
}

