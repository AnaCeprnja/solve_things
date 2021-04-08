import collections
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n,k=map(int, input().split())
    arr = [int(i) for i in input().split()]
    d=collections.deque(arr)
    d.rotate(-k)
    fin = list(d)
    print(' '.join(str(i) for i in d))