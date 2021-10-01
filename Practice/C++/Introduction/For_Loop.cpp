#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a, b;
    cin >> a >> b;
    for (int i = a; i <= b; i++)
    {
        if (i <= 9)
        {
            switch(i)
            {
                case 1: {std::cout << "one\n"; break;}
                case 2: {std::cout << "two\n"; break;}
                case 3: {std::cout << "three\n"; break;}
                case 4: {std::cout << "four\n"; break;}
                case 5: {std::cout << "five\n"; break;}
                case 6: {std::cout << "six\n"; break;}
                case 7: {std::cout << "seven\n"; break;}
                case 8: {std::cout << "eight\n"; break;}
                case 9: {std::cout << "nine\n"; break;}
                default: {std::cout << "zero\n";break;}
            }
        }
        else if (i % 2 == 0) std::cout << "even\n";
        else std::cout << "odd\n";
    }

    return(0);
}

