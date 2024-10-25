from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, nums, k):
        ht = defaultdict(lambda: 0)
        for x in nums:
            ht[x] += 1
        max_item = max(ht.keys())
        if ht[max_item] < k:
            return 0
        global_max_item_in_subarray = 0
        pointer_low = 0
        res = 0
        for pointer_high in range(len(nums)):
            if nums[pointer_high] == max_item:
                global_max_item_in_subarray += 1
            while global_max_item_in_subarray == k:
                if nums[pointer_low] == max_item:
                    global_max_item_in_subarray -= 1
                pointer_low += 1
            res += pointer_low
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,3,2,3,3], 2 #6
    input2 = [1,4,2,1], 3 #0
    input3 = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82], 2 #224
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
