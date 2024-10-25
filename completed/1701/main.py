from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, customers: List[List[int]]) -> float:
        accumulated_preparation_time = customers[0][0]
        res = 0
        for arrival_time, preparation_time in customers:
            if arrival_time > accumulated_preparation_time:
                accumulated_preparation_time = arrival_time
            accumulated_preparation_time += preparation_time
            res += accumulated_preparation_time - arrival_time
        return res / len(customers)


if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,2],[2,5],[4,3]]  # 5
    input2 = [[5,2],[5,4],[10,3],[20,1]]  # 3.25
    input3 = [[5,2],[5,4],[10,3],[13,1]]  # 3.5
    input4 = [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]  # 4.1666
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
