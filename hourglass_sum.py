#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    temp = -60
    for i in range(4):
        for j in range(4):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] + arr[i+1][j+1]
            if total > temp:
                temp = total
    return temp

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(str(result) + '\n')
