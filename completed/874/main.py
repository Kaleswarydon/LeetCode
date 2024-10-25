from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {tuple(o) for o in obstacles}
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        current_dir = 0
        x = 0
        y = 0
        res = 0
        for c in commands:
            if c == -1:
                current_dir = (current_dir + 1) % 4
            elif c == -2:
                current_dir = (current_dir + 3) % 4
            else:
                for _ in range(c):
                    dx = dirs[current_dir][0]
                    dy = dirs[current_dir][1]
                    if (x + dx, y + dy) in obstacles:
                        break
                    x += dx
                    y += dy
            res = max(res, (x ** 2) + (y ** 2))
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [4,-1,3], []  # 25
    input2 = [4,-1,4,-2,4], [[2,4]]  # 65
    input3 = [6,-1,-1,6], []  # 36
    print(sol.robotSim(*input1))
    print(sol.robotSim(*input2))
    print(sol.robotSim(*input3))
