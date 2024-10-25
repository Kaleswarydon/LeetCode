from icecream import ic as print
from collections import defaultdict
import heapq

class Solution:
    def dummy(self, nums):
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for j in range(len(nums) - 2, -1, -1):
            right[j] = right[j + 1] * nums[j+1]
        return [a * b for (a, b) in zip(left, right)]

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,4]
    input2 = [-1,1,0,-3,3]
    print(sol.dummy(input1))
    print(sol.dummy(input2))
