from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def helper(self, nums, minK, maxK):
        # simply counts all sub arrays that dont include minK and maxK and subtract from total sub arrays
        if not nums:
            return 0
        res = 0
        pointer_low = 0
        pointer_high = 0
        ht = defaultdict(lambda: 0) #could be optimized, no need for a whole dict - just trace min/max
        while pointer_high < len(nums):
            ht[nums[pointer_high]] += 1
            while ht[minK] and ht[maxK] and pointer_low <= pointer_high:
                ht[nums[pointer_low]] -= 1
                pointer_low += 1
            res += pointer_high - pointer_low + 1
            pointer_high += 1
        return ((len(nums) * (len(nums) + 1)) // 2) - res

    def countSubarrays(self, nums, minK, maxK):
        # split array into sub arrays that only contain values mink <= val <= maxK
        split_indices = [i for i, x in enumerate(nums) if x < minK or x > maxK] + [len(nums)]
        res = 0
        prev = 0
        for y in split_indices:
            res += self.helper(nums[prev:y], minK, maxK)  # add up results from "valid" sub arrays
            prev = y + 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,3,5,2,7,5], 1, 5 #2
    input2 = [1,1,1,1], 1, 1 #10
    input3 = [1,3,5,2,4,5], 1, 5 #4
    print(sol.countSubarrays(*input1))
    print(sol.countSubarrays(*input2))
    print(sol.countSubarrays(*input3))
