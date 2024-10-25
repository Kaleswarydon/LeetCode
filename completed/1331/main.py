from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        ranks = {}
        pq = []
        for i, x in enumerate(arr):
            heapq.heappush(pq, (x, i))
        curr_rnk = 1
        while pq:
            val, ind = heapq.heappop(pq)
            tmp = ranks.get(val)
            if tmp:
                res[ind] = tmp
            else:
                res[ind] = curr_rnk
                ranks[val] = curr_rnk
                curr_rnk += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [40,10,20,30] #  [4,1,2,3]
    input2 = [100,100,100] #  [1,1,1]
    input3 = [37,12,28,9,100,56,80,5,12]  # [5,3,4,2,8,6,7,1,3]
    print(sol.arrayRankTransform(input1))
    print(sol.arrayRankTransform(input2))
    print(sol.arrayRankTransform(input3))
