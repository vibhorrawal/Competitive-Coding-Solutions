'''
Sorting: Bubble Sort

Sample Input 0

3
1 2 3

Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a,n):
    c = 0
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                c+=1
    print("Array is sorted in {} swaps.".format(c))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[n-1]))



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a,n)

