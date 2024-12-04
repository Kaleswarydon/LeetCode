from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        r = len(arr)
        for j in range(len(arr) - 2, -1, -1):
            if arr[j] > arr[j+1]:
                r = j + 1
                break
        if r == len(arr):
            return 0
        min_remove = r
        prev = -1
        for l in range(len(arr)):
            while r < len(arr) and arr[l] > arr[r]:
                r += 1
            if prev > arr[l]:
                break
            min_remove = min(min_remove, r - (l + 1))
            prev = arr[l]
        return min_remove


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,10,4,2,3,5]  # 3
    input2 = [5,4,3,2,1]  # 4
    input3 = [1,2,3]  # 0
    input4 = [1,2,3,4,5]  # 0
    input5 = [1,2,3,10,0,7,8,9]  # 2
    input6 = [1,3,2,4]  # 1
    input7 = [10,13,17,21,15,15,9,17,22,22,13]  # 7
    print(sol.findLengthOfShortestSubarray(input1))
    print(sol.findLengthOfShortestSubarray(input2))
    print(sol.findLengthOfShortestSubarray(input3))
    print(sol.findLengthOfShortestSubarray(input4))
    print(sol.findLengthOfShortestSubarray(input5))
    print(sol.findLengthOfShortestSubarray(input6))
    print(sol.findLengthOfShortestSubarray(input7))
