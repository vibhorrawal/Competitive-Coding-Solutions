'''
Given  arrays  of different sizes, find the number of distinct triplets  where  is an element of , written as , , and , satisfying the criteria: .

For example, given  and , we find four distinct triplets: .

Function Description

Complete the triplets function in the editor below. It must return the number of distinct triplets that can be formed from the given arrays.

triplets has the following parameter(s):

a, b, c: three arrays of integers .
Input Format

The first line contains  integers , the sizes of the three arrays. 
The next  lines contain space-separated integers numbering  respectively.

Constraints



Output Format

Print an integer representing the number of distinct triplets.
Sample Input

3 2 3
1 3 5
2 3
1 2 3
Sample Output

8 
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b= list(sorted(set(b)))
    c = list(sorted(set(c)))
    an = 0
    bn = 0
    cn = 0
    ans = 0
    
    while bn < len(b):
        while an < len(a) and a[an] <= b[bn]:
            an += 1
        
        while cn < len(c) and c[cn] <= b[bn]:
            cn += 1
        
        ans += an * cn
        bn += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
