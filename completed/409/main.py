from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, s):
        res = 0
        hist = defaultdict(lambda: 0)
        for x in s:
            hist[ord(x)] += 1
        for y in hist:
            tmp = (hist[y] // 2) * 2
            hist[y] -= tmp
            res += tmp
        if any(hist.values()):
            res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "abccccdd"
    input2 = "a"
    print(sol.dummy(input1))
    print(sol.dummy(input2))
