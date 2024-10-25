from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        tmp = []
        for ind, x in enumerate(nums):
            tmp.append((int(''.join([str(mapping[int(i)]) for i in list(str(x))])), ind, x))
        tmp.sort(key=lambda y: y)
        return [z[2]for z in tmp]


if __name__ == '__main__':
    sol = Solution()
    input1 = [8,9,4,0,2,1,3,5,7,6], [991,338,38]  # [338,38,991]
    input2 = [0,1,2,3,4,5,6,7,8,9], [789,456,123]  # [123,456,789]
    print(sol.sortJumbled(*input1))
    print(sol.sortJumbled(*input2))
