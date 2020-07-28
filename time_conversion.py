#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    h, m, ss = map(int, s[:-2].split(':'))
    t = s[-2:]
    h = h % 12 + (t.upper() == 'PM') * 12
    string = ('%02d:%02d:%02d' % (h, m, ss))
    return string
        

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
    # f.write(result + '\n')

    # f.close()
