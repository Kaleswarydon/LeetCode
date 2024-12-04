from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        all_teams = set([x for x in range(n)])
        has_lost = set()
        for w, l in edges:
            has_lost.add(l)
        res = all_teams.difference(has_lost)
        if len(res) != 1:
            return -1
        return res.pop()

if __name__ == '__main__':
    sol = Solution()
    input1 = 3, [[0,1],[1,2]]  # 0
    input2 = 4, [[0,2],[1,3],[1,2]]  # -1
    print(sol.findChampion(*input1))
    print(sol.findChampion(*input2))
