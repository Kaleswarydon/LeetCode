from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, happiness, k):
        happiness = [-x for x in happiness]
        heapq.heapify(happiness)
        res = 0
        for i in range(k):
            tmp = abs(heapq.heappop(happiness)) - i
            res += tmp if tmp > 0 else 0
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3], 2
    input2 = [1,1,1,1], 2
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
