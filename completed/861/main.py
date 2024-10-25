from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:


    def dummy(self, grid):
        def get_bit_score(bit_list):
            res_score = 0
            for j in range(len(bit_list)):
                res_score += bit_list[len(bit_list) - 1 - j] * (2 ** j)
            return res_score

        # process rows
        for i in range(len(grid)):
            if get_bit_score(grid[i]) < get_bit_score(grid[i][::1]) or not grid[i][0]:
                grid[i] = [int(not x) for x in grid[i]]

        # process columns
        grid = list(zip(*grid))
        for i in range(len(grid)):
            if sum(grid[i]) < len(grid[i]) / 2:
                grid[i] = [int(not x) for x in grid[i]]
        res_grid = list(zip(*grid))

        # process bit score
        res_score = 0
        for i in range(len(res_grid)):
            res_score += get_bit_score(res_grid[i])

        return res_score

if __name__ == '__main__':
    sol = Solution()
    input1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]] #39
    input2 = [[0]] #1
    input3 = [[0,1],[0,0]] #5
    input4 = [[0,1,0],[0,0,1]] #11
    input5 = [[0,1],[1,1]] #5
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
    print(sol.dummy(input5))
