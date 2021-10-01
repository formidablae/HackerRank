#include <stdio.h>

void update(int *posOne,int *posTwo)
{
     int sum, diff;
     sum = *posOne + *posTwo;
     if (*posOne > *posTwo) diff = *posOne - *posTwo;
     else diff = *posTwo - *posOne;

     *posOne = sum;
     *posTwo = diff;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

