#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    char ch1[100];
    char ch2[100];
    char ch3[100];

    scanf("%[^\n]%*c\n", &ch1);
    scanf("%[^\n]%*c\n", &ch2);
    scanf("%[^\n]%*c\n", &ch3);

    printf("%s\n", ch1);
    printf("%s\n", ch2);
    printf("%s\n", ch3);

    return 0;
}

