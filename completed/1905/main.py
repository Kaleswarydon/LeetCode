from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List

null = None


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def is_valid_coord(coord, dims):
            c1, c2 = coord
            d1, d2 = dims
            return 0 <= c1 < d1 and 0 <= c2 < d2

        def find_islands(g):
            islands = []
            for i in range(len(g)):
                for j in range(len(g[0])):
                    if g[i][j]:
                        islands.append(bfs(g, (i, j)))
            return islands

        def bfs(g: List[List[int]], start: tuple):
            res = []
            q = deque([start])
            while q:
                item = q.popleft()
                res.append(tuple(item))
                for neigh in [(item[0] - 1, item[1]), (item[0], item[1] - 1), (item[0] + 1, item[1]), (item[0], item[1] + 1)]:
                    if is_valid_coord(neigh, [len(g), len(g[0])]) and g[neigh[0]][neigh[1]]:
                        g[neigh[0]][neigh[1]] = 0
                        q.append(neigh)
            return res

        islands_grid2 = find_islands(grid2)
        res = 0
        for i2 in islands_grid2:
            valid_sub = True
            for ti, tj in i2:
                if not grid1[ti][tj]:
                    valid_sub = False
                    break
            if valid_sub:
                res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = ([[1, 1, 1, 0, 0],
              [0, 1, 1, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [1, 1, 0, 1, 1]],
              [[1, 1, 1, 0, 0],
              [0, 0, 1, 1, 1],
               [0, 1, 0, 0, 0],
               [1, 0, 1, 1, 0],
               [0, 1, 0, 1,0]])  # 3
    input2 = ([[1, 0, 1, 0, 1],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1],
              [1, 0, 1, 0, 1]],
              [[0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1],
               [0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0],
               [1, 0, 0, 0, 1]])  # 2
    input3 = ([[1,1,1,1,0,0],
              [1,1,0,1,0,0],
              [1,0,0,1,1,1],
              [1,1,1,0,0,1],
              [1,1,1,1,1,0],
              [1,0,1,0,1,0],
              [0,1,1,1,0,1],
              [1,0,0,0,1,1],
              [1,0,0,0,1,0],
              [1,1,1,1,1,0]],
              [[1,1,1,1,0,1],
               [0,0,1,0,1,0],
               [1,1,1,1,1,1],
               [0,1,1,1,1,1],
               [1,1,1,0,1,0],
               [0,1,1,1,1,1],
               [1,1,0,1,1,1],
               [1,0,0,1,0,1],
               [1,1,1,1,1,1],
               [1,0,0,1,0,0]])
    print(sol.countSubIslands(*input1))
    print(sol.countSubIslands(*input2))
    print(sol.countSubIslands(*input3))
