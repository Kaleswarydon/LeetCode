from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(pq)
        res = "_"
        tmp = (None, None)
        while pq:
            r = 2
            curr_remaining, curr_char = heapq.heappop(pq)
            if res[-1] == curr_char:
                tmp = (curr_remaining, curr_char)
                if not pq:
                    break
                curr_remaining, curr_char = heapq.heappop(pq)
                r = 1
            for x in range(r):
                if not curr_remaining:
                    break
                res += curr_char
                curr_remaining += 1
            if curr_remaining < 0:
                heapq.heappush(pq, (curr_remaining, curr_char))
            if not None in tmp:
                heapq.heappush(pq, tmp)
                tmp = (None, None)
        return res[1:]


if __name__ == '__main__':
    sol = Solution()
    input1 = 1, 1, 7  # "ccaccbcc"
    input2 = 7, 1, 0  # "aabaa"
    input3 = 2, 2, 1  # 'aabbc'
    input4 = 0, 8, 11  # "ccbccbbccbbccbbccbc"
    print(sol.longestDiverseString(*input1))
    print(sol.longestDiverseString(*input2))
    print(sol.longestDiverseString(*input3))
    print(sol.longestDiverseString(*input4))
