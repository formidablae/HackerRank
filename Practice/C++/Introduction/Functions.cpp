#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int max_of_four(int a, int b, int c, int d)
{
    int max = a;
    std::vector<int> aVector;
    aVector.push_back(a);
    aVector.push_back(b);
    aVector.push_back(c);
    aVector.push_back(d);

    for (int i = 0; i < aVector.size(); i++)
    {
        if (aVector[i] > max)
        {
            max = aVector[i];
        }
    }

    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

