#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int numbers;
    cin >> numbers;
    std::vector<int> aVector;
    for (int i = 0; i < numbers; i++)
    {
        int newNumb;
        cin >> newNumb;
        aVector.push_back(newNumb);
    }

    for (int i = numbers - 1; i >= 0; i--)
    {
        cout << aVector[i] << " ";
    }
    return 0;
}

