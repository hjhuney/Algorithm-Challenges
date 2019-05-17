#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):


    column_nums_below = [0]
    column_nums_above = [n+1]

    for row in obstacles:
        if row[0] == r_q:
            if row[1] > c_q:
                column_nums_above.append(row[1])
            elif row[1] < c_q:
                column_nums_below.append(row[1])
                
    moves_left = c_q - min(column_nums_below, key=lambda x: c_q-x) - 1
    moves_right = min(column_nums_above, key=lambda x: x-c_q) - c_q - 1

    hor_moves = moves_left + moves_right

    # calculate vertical moves

    row_nums_below = [0]
    row_nums_above = [n+1]

    for row in obstacles:

        if row[1] == c_q:
            if row[0] > r_q:
                row_nums_above.append(row[0])
            elif row[0] < r_q:
                row_nums_below.append(row[0])

    moves_south = r_q - min(row_nums_below, key=lambda x: r_q-x) - 1
    moves_north= min(row_nums_above, key=lambda x: x-r_q) - r_q - 1

    ver_moves = moves_north + moves_south   

    # calculate diagonals left

    check_row = r_q - 1
    check_column = c_q - 1
    count = 0
    diag_moves = 0

    while (check_row > 0) & (check_column > 0):
        if [check_row, check_column] in obstacles:
            diag_moves += count
            break
        else:
            count +=1
            check_row -= 1
            check_column -= 1
            if (check_row == 0) or (check_column == 0):
                diag_moves += count
            
    check_row = r_q + 1
    check_column = c_q -1
    count = 0     
            
    while (check_row < n+1) & (check_column > 0):
        if [check_row, check_column] in obstacles:
            diag_moves += count
            break
        else:
            count +=1
            check_row += 1
            check_column -= 1
            if (check_row == n+1) or (check_column == 0):
                diag_moves += count

    # calculate diagonals right
        
    check_row = r_q + 1
    check_column = c_q + 1
    count = 0

    while (check_row < n+1) & (check_column < n+1):
        if [check_row, check_column] in obstacles:
            diag_moves += count
            break
        else:
            count +=1
            check_row += 1
            check_column += 1
            if (check_row == n+1) or (check_column == n+1):
                diag_moves += count   
            
            
    check_row = r_q - 1
    check_column = c_q + 1
    count = 0

    while (check_row > 0) & (check_column < n+1):
        if [check_row, check_column] in obstacles:
            diag_moves += count
            break
        else:
            count +=1
            check_row -= 1
            check_column += 1
            if (check_row == 0) or (check_column == n+1):
                diag_moves += count     
                

    # calculate total moves
    total_moves = hor_moves + ver_moves + diag_moves

    return total_moves
    

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
