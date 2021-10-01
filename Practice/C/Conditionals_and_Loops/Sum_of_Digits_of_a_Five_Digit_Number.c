#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    int m1, m2, m3, m4, m5, sum;

    scanf("%d", &n);

    m5 = n % 10;
    m4 = ((n - m5) % 100) / 10;
    m3 = ((n - m4 * 10 - m5) % 1000) / 100;
    m2 = ((n - m3 * 100 - m4 * 10 - m5) % 10000) / 1000;
    m1 = ((n - m2 * 1000 - m3 * 100 - m4 * 10 - m5) % 100000) / 10000;

    sum = m1 + m2 + m3 + m4 + m5;

    printf("%d", sum);
    return 0;
}

