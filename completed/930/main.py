from icecream import ic as print
from collections import defaultdict
import heapq

class Solution:
    def _worker(self, nums, goal):
        if goal < 0:
            return 0
        pointer_low = 0
        running_sum = 0
        res = 0
        for pointer_high, item in enumerate(nums):
            running_sum += nums[pointer_high]
            while running_sum > goal:
                running_sum -= nums[pointer_low]
                pointer_low += 1
            res += pointer_high - pointer_low + 1
        return res

    def dummy(self, nums, goal):
        return self._worker(nums, goal) - self._worker(nums, goal - 1)

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,0,1,0,1], 2
    input2 = [0,0,0,0,0], 0
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
