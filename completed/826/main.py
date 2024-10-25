from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pq = []
        for i in range(len(difficulty)):
            heapq.heappush(pq, (-profit[i], difficulty[i]))
        worker.sort(reverse=True)
        res = 0
        for w in worker:
            while pq:
                tmp = heapq.heappop(pq)
                if w >= tmp[1]:
                    res += tmp[0]
                    heapq.heappush(pq, tmp)
                    break
        return -res

if __name__ == '__main__':
    sol = Solution()
    input1 = [2,4,6,8,10], [10,20,30,40,50], [4,5,6,7] # 100
    input2 = [85,47,57], [24,66,99], [40,25,25] # 0
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
