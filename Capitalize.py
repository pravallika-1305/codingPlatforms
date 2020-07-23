#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new = s.split()
    final_string = ""
    final_string = final_string + new[0].capitalize()
    for i in range(1,len(new)):
        final_string = final_string + " "
        final_string = final_string + new[i].capitalize()
    return final_string
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
