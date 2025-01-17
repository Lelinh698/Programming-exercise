#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if grade < 38:
            temp = grade
        elif (grade % 5 >= 3):
            temp = grade - grade % 5 + 5
        else:
            temp = grade
        result.append(temp)
    return result
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    
    print('\n')
    print(' '.join(map(str, result)))
    

    # fptr.close()
