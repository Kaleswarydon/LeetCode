from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, seats: List[int], students: List[int]) -> int:
        seats_s = sorted(seats)
        students_s = sorted(students)
        res = 0
        for i in range(len(seats)):
            res += abs(seats_s[i] - students_s[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [3,1,5], [2,7,4] # 4
    input2 = [4,1,5,9], [1,3,2,6] # 7
    input3 = [2,2,6,6], [1,3,2,6] # 4
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
