#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    
    // Declare second integer, double, and String variables.
    int ii;
    double dd;
    std::string ss;
    // Read and save an integer, double, and String to your variables.
    cin >> ii;
    cin >> dd;
    getline(cin >> ws, ss);
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    
    // Print the sum of both integer variables on a new line.
    cout << i + ii << endl;
    // Print the sum of the double variables on a new line.
    std::cout << std::fixed;
    std::cout << std::setprecision(1);
    cout << d + dd << endl;
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout << s + ss << endl;
    return 0;
}
