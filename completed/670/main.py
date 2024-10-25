from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(d) for d in str(num)]
        pq = []
        for i, k in enumerate(num):
            heapq.heappush(pq, (-k, i))
        for j, l in enumerate(num):
            if -pq[0][0] > l:
                x, y = heapq.heappop(pq)
                max_y = y
                while pq[0][0] == x:
                    _, y = heapq.heappop(pq)
                    max_y = max(max_y, y)
                num[j] = -x
                num[max_y] = l
                break
            if -pq[0][0] == l:
                heapq.heappop(pq)
        return int(''.join([str(z) for z in num]))


if __name__ == '__main__':
    sol = Solution()
    input1 = 2736  # 7236
    input2 = 9973  # 9973
    input3 = 98368  # 98863
    input4 = 1993  # 9913
    print(sol.maximumSwap(input1))
    print(sol.maximumSwap(input2))
    print(sol.maximumSwap(input3))
    print(sol.maximumSwap(input4))
