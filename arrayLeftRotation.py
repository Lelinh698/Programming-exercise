#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    temp = []
    for i in range(d, len(a)):
        temp.append(a[i])

    for i in range(0, d):
        temp.append(a[i])

    return temp

if __name__ == '__main__':
    nd = input().split()

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(' '.join(map(str, result)))
    print('\n')
