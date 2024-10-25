from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List

null = None


class Solution:
    def expand_grid(self, grid):
        def fill_grid(x, y, symb):
            g[x][y] = 1
            if symb == '\\':
                g[x - 1][y - 1] = 1
                g[x + 1][y + 1] = 1
            if symb == '/':
                g[x - 1][y + 1] = 1
                g[x + 1][y - 1] = 1
        g = [[0 for y in range(len(grid[0]) * 3)] for x in range(len(grid) * 3)]
        cntr1 = 0
        cntr2 = 0
        for i in range(1, len(g), 3):
            for j in range(1, len(g[0]), 3):
                if grid[cntr1][cntr2] != ' ':
                    fill_grid(i, j, grid[cntr1][cntr2])
                cntr2 += 1
            cntr1 += 1
            cntr2 = 0
        return g

    def regionsBySlashes(self, grid: List[str]) -> int:
        def bfs(k, l):
            assert not g[k][l]
            q = deque([(k, l)])
            while q:
                x, y = q.popleft()
                g[x][y] = 2
                for z1, z2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= z1 < len(g) and 0 <= z2 < len(g[0]) and not g[z1][z2] and (z1, z2) not in q:
                        q.append((z1, z2))
        g = self.expand_grid(grid)
        res = 0
        for i in range(len(g)):
            for j in range(len(g[0])):
                if not g[i][j]:
                    bfs(i, j)
                    res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [" /", "/ "]  # 2
    input2 = [" /", "  "]  # 1
    input3 = ["/\\", "\\/"]  # 5
    input4 = ["//\\\\////","//\\\\/\\//","\\/ /\\\\/\\","///\\\\\\\\ ","//  / \\\\","\\/\\/ //\\"," // \\ \\\\","/\\\\/\\\\\\/"]
    print(sol.regionsBySlashes(input1))
    print(sol.regionsBySlashes(input2))
    print(sol.regionsBySlashes(input3))
    print(sol.regionsBySlashes(input4))
