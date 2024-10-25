from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode


class Solution:
    def dummy(self, nums):
        #floyd's tortoise & hare algo
        pointer_low1 = 0
        pointer_low2 = 0
        pointer_high = 0
        while True: #handle this list as a graph with list values as indices to next node
            pointer_low1 = nums[pointer_low1] #move slow ptr once
            pointer_high = nums[pointer_high] #move fast ptr 2 times
            pointer_high = nums[pointer_high]
            if pointer_low1 == pointer_high: #if there is a cycle, theyll meet somewhere
                break
        while True:
            pointer_low1 = nums[pointer_low1] #slow pointer 1 and 2 will meet at the first node of the cycle
            pointer_low2 = nums[pointer_low2]
            if pointer_low1 == pointer_low2:
                break
        return pointer_low1 #the node both pointers are pointing at is the result


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,3,4,2,2] #2
    input2 = [3,1,3,4,2] #3
    input3 = [3,3,3,3,3] #3
    input4 = [2,3,3,3,4] #3
    input5 = [2,3,4,4,4,4,5] #4
    input6 = [1,4,4,2,4] #4
    input7 = [2,1,1,1,4] #1
    input8 = [8,1,1,1,2,7,4,3,1,1] #1
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
    print(sol.dummy(input5))
    print(sol.dummy(input6))
    print(sol.dummy(input7))
    print(sol.dummy(input8))
