from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        pq = [(0, 0, 0)]
        while pq:
            curr_cost, curr_x, curr_y = heapq.heappop(pq)
            for d_x, d_y in directions:
                tmp_x = curr_x + d_x
                tmp_y = curr_y + d_y
                if 0 <= tmp_x < len(grid) and 0 <= tmp_y < len(grid[0]):
                    new_cost = curr_cost + (grid[tmp_x][tmp_y] - curr_cost) + ((grid[tmp_x][tmp_y] - curr_cost + 1) % 2)
                    if grid[tmp_x][tmp_y] <= curr_cost:
                        new_cost = curr_cost + 1
                    if tmp_x == len(grid) - 1 and tmp_y == len(grid[0]) - 1:
                        return new_cost
                    if grid[tmp_x][tmp_y] != -1:
                        heapq.heappush(pq, (new_cost, tmp_x, tmp_y))
                        grid[tmp_x][tmp_y] = -1


if __name__ == '__main__':
    sol = Solution()
    input1 = [[0,1,3,2],
              [5,1,2,5],
              [4,3,8,6]]  # 7
    input2 = [[0,2,4],
              [3,2,1],
              [1,0,4]]  # -1
    input3 = [[0,2,4],
              [0,5,5],
              [5,4,3]]  # 6
    print(sol.minimumTime(input1))
    print(sol.minimumTime(input2))
    print(sol.minimumTime(input3))
