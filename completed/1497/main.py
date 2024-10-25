from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)
        for x in arr:
            freq[((x % k) + k) % k] += 1
        #print(freq)
        for i in range(1, k):
            if freq[i] != freq[k-i]:
                #print(freq[i], freq[k - i])
                return False
        if freq[0]:
            return not bool(freq[0] % 2)
        return True

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,4,5,10,6,7,8,9], 5  # True
    input2 = [1,2,3,4,5,6], 7  # True
    input3 = [1,2,3,4,5,6], 10  # False
    input4 = [-1,1,-2,2,-3,3,-4,4], 3  # True
    input5 = [8,6,3,3], 5 # False
    input6 = [-10,10], 2  # True
    print(sol.canArrange(*input1))
    print(sol.canArrange(*input2))
    print(sol.canArrange(*input3))
    print(sol.canArrange(*input4))
    print(sol.canArrange(*input5))
    print(sol.canArrange(*input6))
