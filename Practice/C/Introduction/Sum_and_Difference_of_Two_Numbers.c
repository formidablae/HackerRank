#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int firstRowFirstNum, firstRowSecondNum, sumInt, diffInt;
    float secondRowFirstNum, secondRowSecondNum, sumFloat, diffFloat;

    scanf("%d %d\n", &firstRowFirstNum, &firstRowSecondNum);
    scanf("%f %f", &secondRowFirstNum, &secondRowSecondNum);

    sumInt = firstRowFirstNum + firstRowSecondNum;
    diffInt = firstRowFirstNum - firstRowSecondNum;

    sumFloat = secondRowFirstNum + secondRowSecondNum;
    diffFloat = secondRowFirstNum - secondRowSecondNum;

    printf("%d %d\n", sumInt, diffInt);
    printf("%.1f %.1f\n", sumFloat, diffFloat);
    return 0;
}

