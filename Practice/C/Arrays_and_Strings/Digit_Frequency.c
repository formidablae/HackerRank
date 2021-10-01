#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char s[1000];
    int zeros = 0;
    int ones = 0;
    int twos = 0;
    int threes = 0;
    int fours = 0;
    int fives = 0;
    int sixs = 0;
    int sevens = 0;
    int eights = 0;
    int nines = 0;
    scanf("%s", s);
    // printf(s);
    for (int i = 0; s[i]!='\0'; i++)
    {
        if(s[i] == '0') zeros++;
        else if(s[i] == '1') ones++;
        else if(s[i] == '2') twos++;
        else if(s[i] == '3') threes++;
        else if(s[i] == '4') fours++;
        else if(s[i] == '5') fives++;
        else if(s[i] == '6') sixs++;
        else if(s[i] == '7') sevens++;
        else if(s[i] == '8') eights++;
        else if(s[i] == '9') nines++;
    }

    printf("%d %d %d %d %d %d %d %d %d %d", zeros, ones, twos, threes, fours, fives, sixs, sevens, eights, nines);

    return 0;
}

