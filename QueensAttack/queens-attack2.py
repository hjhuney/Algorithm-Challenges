#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    ObSet = set(tuple(x) for x in obstacles)
    Delta = [(0,1),(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(1,-1),(-1,1)]
    Count = 0
    for shift in Delta:
        Pos = (r_q,c_q)
        while Pos[0] + shift[0] >=1 and Pos[0] + shift[0] <= n and Pos[1] + shift[1] >=1 and Pos[1] + shift[1] <= n:
            Pos = (Pos[0]+shift[0],Pos[1]+shift[1])
            if Pos in ObSet:
                break
            Count += 1

    return Count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    
    fptr.write(str(result) + '\n')

    fptr.close()
