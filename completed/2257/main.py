from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def traverse(start, step, ft):
            curr_x, curr_y = start
            step_x, step_y, val = step
            if not grid[curr_x][curr_y]:
                ft -= 1
            grid[curr_x][curr_y] = 3
            curr_x += step_x
            curr_y += step_y
            while 0 <= curr_x < len(grid) and 0 <= curr_y < len(grid[0]):
                if grid[curr_x][curr_y]:
                    if grid[curr_x][curr_y] == 3 or not grid[curr_x][curr_y] % val:
                        break
                    else:
                        grid[curr_x][curr_y] *= val
                else:
                    grid[curr_x][curr_y] = val
                    ft -= 1
                curr_x += step_x
                curr_y += step_y
            return ft
        grid = [[0 for _ in range(n)] for _ in range(m)]
        free_tiles = m * n
        for wx, wy in walls:
            grid[wx][wy] = 3
            free_tiles -= 1
        for g in guards:
            for d in [[0, -1, 5], [0, 1, 5], [-1, 0, 7], [1, 0, 7]]:
                free_tiles = traverse(tuple(g), d, free_tiles)
        #print(grid)
        return free_tiles

if __name__ == '__main__':
    sol = Solution()
    input1 = 4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]  # 7
    input2 = 3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]  # 4
    print(sol.countUnguarded(*input1))
    print(sol.countUnguarded(*input2))
