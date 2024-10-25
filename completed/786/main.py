from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, arr, k):
        h = []
        for i in range(1, len(arr)):
            heapq.heappush(h, (1 / arr[i], (0, i)))
        numerator_ind, denominator_ind = -1, -1
        for j in range(k):
            try:
                _, (numerator_ind, denominator_ind) = heapq.heappop(h)
            except:
                return [arr[-1], arr[-1]]
            if numerator_ind < len(arr) - 1:
                numerator_ind += 1
                heapq.heappush(h, (arr[numerator_ind] / arr[denominator_ind], (numerator_ind, denominator_ind)))
        return [arr[numerator_ind - 1], arr[denominator_ind]]

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,5], 3
    input2 = [1,7], 1
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
