from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def get_prefixes(n: int):
            tmp = str(n)
            res = []
            for i in range(len(tmp)):
                res.append(tmp[:i + 1])
            return res
        ht = set()
        for x in arr1:
            ht.update(get_prefixes(x))
        res = 0
        for y in arr2:
            for z in get_prefixes(y):
                if z in ht:
                    res = max(res, len(z))
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,10,100], [1000]  # 3
    input2 = [1,2,3], [4,4,4]  # 0
    print(sol.longestCommonPrefix(*input1))
    print(sol.longestCommonPrefix(*input2))
