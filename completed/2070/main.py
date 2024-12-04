from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        res = [0] * len(queries)
        j = 0
        curr_max_b = 0
        for q, i in sorted([(q, i) for i, q in enumerate(queries)]):
            while j < len(items) and q >= items[j][0]:
                curr_max_b = max(curr_max_b, items[j][1])
                j += 1
            res[i] = curr_max_b
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]  # [2,4,5,5,6,6]
    input2 = [[1,2],[1,2],[1,3],[1,4]], [1]  # [4]
    input3 = [[10,1000]], [5]  # [0]
    print(sol.maximumBeauty(*input1))
    print(sol.maximumBeauty(*input2))
    print(sol.maximumBeauty(*input3))
