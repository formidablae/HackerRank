//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender)
{
  //Write your code here.
    int sum = 0;
    for (int i = 0; i < number_of_students; i++)
    {
        if (gender == 'b' && i % 2 == 0)
        {
            sum = sum + *(marks + i);
        }
        else if (gender == 'g' && i % 2 == 1)
        {
            sum = sum + *(marks + i);
        }
    }

    return sum;
}

