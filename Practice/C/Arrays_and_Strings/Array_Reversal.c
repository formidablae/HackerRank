#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }


    /* Write the logic to reverse the array. */
    int *newArr;
    newArr = (int*) malloc(num * sizeof(int));
    for(int j = 0; j < num; j++)
    {
        newArr[j] = arr[num-j-1];
    }

    for(i = 0; i < num; i++)
        printf("%d ", *(newArr + i));
    return 0;
}

