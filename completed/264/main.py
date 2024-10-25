from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq = [2, 3, 5]
        heapq.heapify(pq)
        res = 0
        curr_prime = 1
        while res < n - 1:
            curr_prime = heapq.heappop(pq)
            tmp = [curr_prime * 2, curr_prime * 3, curr_prime * 5]
            for t in tmp:
                if t not in pq and len(pq) < n - 1:
                    heapq.heappush(pq, t)
            res += 1
        return curr_prime

if __name__ == '__main__':
    sol = Solution()
    input1 = 10  # 12
    input2 = 1  # 1
    print(sol.nthUglyNumber(input1))
    print(sol.nthUglyNumber(input2))
