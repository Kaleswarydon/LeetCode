from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def is_valid_coord(self, x, y, dim_x, dim_y):
        return 0 <= x < dim_x and 0 <= y < dim_y
    def minDays(self, grid: List[List[int]]) -> int:
        def helper(c):
            def bfs(k, l):
                q = deque([(k, l)])
                current_val = grid[k][l]
                while q:
                    x, y = q.popleft()
                    grid[x][y] = current_val + 1
                    for z1, z2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if 0 <= z1 < len(grid) and 0 <= z2 < len(grid[0]) and grid[z1][z2] == current_val and (z1, z2) not in q:
                            q.append((z1, z2))

            islands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == c:
                        islands += 1
                        bfs(i, j)
                        if islands > 1:
                            return 0
            return islands

        res = helper(1)
        if not res:
            return res
        island_cells = 0
        for u in range(len(grid)):
            for v in range(len(grid[0])):
                if grid[u][v]:
                    c = grid[u][v]
                    grid[u][v] = 0
                    tmp = helper(c)
                    if tmp != res:
                        return 1
                    grid[u][v] = c + 1
                    #print(res)
                    island_cells += 1
        if island_cells == 1:
            return 1
        return 2



if __name__ == '__main__':
    sol = Solution()
    input1 = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]  # 2
    input2 = [[1,1]]  # 2
    input3 = [[1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1]]  # 2
    input4 = [[1,0,1,1,1,0,1,1,1,1,1],[1,0,1,1,0,0,0,1,1,0,1],[0,0,1,1,1,1,0,1,1,1,0],[1,1,1,1,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,1,0],[0,1,0,1,1,1,1,1,1,0,1],[1,1,1,1,1,1,0,1,1,1,1],[1,1,1,0,0,1,1,1,1,1,1],[0,1,1,1,1,1,1,0,1,1,1]]  # 0
    input5 = [[1,1,0],[1,1,1],[0,1,0]]  # 1
    input6 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]  # 2
    input7 = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]  # 1
    input8 = [[1,0],[1,1]]  # 1
    input9 = [[0,0]]  # 0
    print(sol.minDays(input1))
    print(sol.minDays(input2))
    print(sol.minDays(input3))
    print(sol.minDays(input4))
    print(sol.minDays(input5))
    print(sol.minDays(input6))
    print(sol.minDays(input7))
    print(sol.minDays(input8))
    print(sol.minDays(input9))
