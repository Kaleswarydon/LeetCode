from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = Counter(word)
        char_heap = []
        for c_key, c_val in char_count.items():
            heapq.heappush(char_heap, (-c_val, c_key))
        cntr = 0
        weight = 1
        res = 0
        while char_heap:
            if cntr and not cntr % 8:
                weight += 1
            amount, _ = heapq.heappop(char_heap)
            res -= weight * amount
            cntr += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "abcde"  # 5
    input2 = "xyzxyzxyzxyz"  # 12
    input3 = "aabbccddeeffgghhiiiiii"  # 24
    print(sol.minimumPushes(input1))
    print(sol.minimumPushes(input2))
    print(sol.minimumPushes(input3))
