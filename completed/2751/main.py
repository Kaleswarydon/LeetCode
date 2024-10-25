from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        robots = []
        for i in range(len(positions)):
            heapq.heappush(robots, [positions[i], healths[i], directions[i]])
        #print(robots)
        while robots:
            current_robot = heapq.heappop(robots)
            #print(current_robot)
            while current_robot and stack and stack[-1][2] == 'R' and current_robot[2] == 'L':  # collision
                stacked_robot = stack.pop()
                if current_robot[1] != stacked_robot[1]:
                    current_robot = current_robot if current_robot[1] > stacked_robot[1] else stacked_robot
                    current_robot[1] -= 1
                else:
                    current_robot = None
            if current_robot:
                stack.append(current_robot)
        if stack:
            res_dict = defaultdict(lambda: None)
            for p, h, _ in stack:
                res_dict[p] = h
            return [res_dict[x] for x in positions if res_dict[x]]
        return stack

if __name__ == '__main__':
    sol = Solution()
    input1 = [5,4,3,2,1], [2,17,9,15,10], "RRRRR"  # [2,17,9,15,10]
    input2 = [3,5,2,6], [10,10,15,12], "RLRL"  # [14]
    input3 = [1,2,5,6], [10,10,11,11], "RLRL"  # []
    input4 = [13,3], [17,2], "LR"  # [16]
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
    print(sol.dummy(*input4))
