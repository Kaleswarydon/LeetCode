from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def helper(self, height, range_to):
        walls = height[0]
        water = 0
        current_lower_index = 0
        for i in range(1, range_to + 1):
            if height[i] >= height[current_lower_index]:
                water += (height[current_lower_index] * (i - current_lower_index)) - walls
                current_lower_index = i
                walls = 0
            walls += height[i]
        return water

    def trap(self, height):
        if len(height) < 3:
            return 0
        max_elem = max(height)
        max_index = height.index(max_elem)
        left = self.helper(height, max_index)
        height = height[::-1]
        right = self.helper(height, len(height) - 1 - max_index)
        return left + right

if __name__ == '__main__':
    sol = Solution()
    input1 = [0,1,0,2,1,0,1,3,2,1,2,1] #6
    input2 = [4,2,0,3,2,5] #9
    input3 = [2,0,2] #2
    print(sol.trap(input1))
    print(sol.trap(input2))
    print(sol.trap(input3))
