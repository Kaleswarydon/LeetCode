from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def helper(self, nums, at_most_k):
        if not at_most_k:
            return 0
        pointer_low = 0
        res = 0
        ht = defaultdict(lambda: 0)
        for pointer_high in range(len(nums)):
            ht[nums[pointer_high]] += 1
            while len(ht) > at_most_k and pointer_low < pointer_high:
                ht[nums[pointer_low]] -= 1
                if not ht[nums[pointer_low]]:
                    del ht[nums[pointer_low]]
                pointer_low += 1
            res += pointer_high - pointer_low + 1
        return res

    def dummy(self, nums, k):
        a = self.helper(nums, k)
        b = self.helper(nums, k - 1)
        print(a,b)
        return a - b

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,1,2,3], 2 #7
    input2 = [1,2,1,3,4], 3 #3
    input3 = [1,2], 1 #2
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
