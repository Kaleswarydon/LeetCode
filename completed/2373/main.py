from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, grid):
        res = []
        for i in range(1, len(grid) - 1):
            maxes = []
            for j in range(1, len(grid[0]) - 1):
                sub_matrix = [
                    grid[i - 1][j - 1],
                    grid[i - 1][j],
                    grid[i - 1][j + 1],
                    grid[i][j - 1],
                    grid[i][j],
                    grid[i][j + 1],
                    grid[i + 1][j - 1],
                    grid[i + 1][j],
                    grid[i + 1][j + 1],
                ]
                maxes.append(max(sub_matrix))
            res.append(maxes)
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    input2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    print(sol.dummy(input1))
    print(sol.dummy(input2))
