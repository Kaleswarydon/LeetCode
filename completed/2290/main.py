from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        pq = [(0, 0, 0)]
        while pq:
            curr_cost, curr_x, curr_y = heapq.heappop(pq)
            for d_x, d_y in directions:
                tmp_x = curr_x + d_x
                tmp_y = curr_y + d_y
                if tmp_x == len(grid) - 1 and tmp_y == len(grid[0]) - 1:
                    return curr_cost + grid[tmp_x][tmp_y]
                if 0 <= tmp_x < len(grid) and 0 <= tmp_y < len(grid[0]):
                    if grid[tmp_x][tmp_y] != -1:
                        heapq.heappush(pq, (curr_cost + grid[tmp_x][tmp_y], tmp_x, tmp_y))
                        grid[tmp_x][tmp_y] = -1


if __name__ == '__main__':
    sol = Solution()
    input1 = [[0,1,1],[1,1,0],[1,1,0]]  # 2
    input2 = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]  # 0
    print(sol.minimumObstacles(input1))
    print(sol.minimumObstacles(input2))
