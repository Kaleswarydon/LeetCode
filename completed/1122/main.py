from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def flatten_list(self, l):
        res = []
        for x in l:
            res.extend(x)
        if res[0] is list:
            return self.flatten_list(res)
        return res

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ht = defaultdict(lambda: 0)
        for i, x in enumerate(arr2):
            ht[x] = i
        res = [[] for k in range(len(arr2))]
        tmp = []
        for z in arr1:
            try:
                res[ht.get(z)].append(z)
            except:
                tmp.append(z)
        res.append(sorted(tmp))
        return self.flatten_list(res)



if __name__ == '__main__':
    sol = Solution()
    input1 = [2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]
    input2 = [28,6,22,8,44,17], [22,28,8,6]
    print(sol.relativeSortArray(*input1))
    print(sol.relativeSortArray(*input2))
