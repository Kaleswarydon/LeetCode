from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ht = defaultdict(lambda: 0)
        for x in nums:
            ht[x] += 1
        cntr = 0
        for i in sorted(ht.keys(), key=lambda y: (ht[y], -y)):
            for j in range(ht[i]):
                nums[cntr] = i
                cntr += 1
        return nums


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,1,2,2,2,3]  # [3,1,1,2,2,2]
    input2 = [2,3,1,3,2]  # [1,3,3,2,2]
    input3 = [-1,1,-6,4,5,-6,1,4,1]  # [5,-1,4,4,-6,-6,1,1,1]
    print(sol.frequencySort(input1))
    print(sol.frequencySort(input2))
    print(sol.frequencySort(input3))
