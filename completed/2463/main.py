from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        def rec(curr_robot, curr_factory):
            if memo[curr_robot][curr_factory] > -1:
                return memo[curr_robot][curr_factory]
            if curr_robot == -1:
                return 0
            if curr_factory == -1:
                return float("inf")
            use_robot_on_factory = abs(robot[curr_robot] - fac[curr_factory]) + rec(curr_robot - 1, curr_factory - 1)
            dont_use_robot_on_factory = rec(curr_robot, curr_factory - 1)
            memo[curr_robot][curr_factory] = min(use_robot_on_factory, dont_use_robot_on_factory)
            return memo[curr_robot][curr_factory]
        fac = sorted([x for y in [[z[0]] * z[1] for z in factory] for x in y])
        robot.sort()
        memo = [[-1 for _ in range(len(fac))] for _ in range(len(robot))]
        return rec(len(robot) - 1, len(fac) - 1)

if __name__ == '__main__':
    sol = Solution()
    input1 = [0,4,6], [[2,2],[6,2]]  # 4
    input2 = [1,-1], [[-2,1],[2,1]]  # 2
    print(sol.minimumTotalDistance(*input1))
    print(sol.minimumTotalDistance(*input2))
