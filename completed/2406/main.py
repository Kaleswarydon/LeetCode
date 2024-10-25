from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heapq.heapify(intervals)
        groups = [0]
        while intervals:
            arrival, department = heapq.heappop(intervals)
            if groups[0] < arrival:
                heapq.heappop(groups)
            heapq.heappush(groups, department)
        return len(groups)


if __name__ == '__main__':
    sol = Solution()
    input1 = [[5,10],[6,8],[1,5],[2,3],[1,10]]  # 3
    input2 = [[1,3],[5,6],[8,10],[11,13]]  # 1
    print(sol.minGroups(input1))
    print(sol.minGroups(input2))
