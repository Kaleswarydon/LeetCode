from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        dq = deque()
        res = 0
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            if not ((len(dq) + nums[i]) % 2):
                if i + k > len(nums):
                    return -1
                dq.append(i)
                res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [0,1,0], 1  # 2
    input2 = [1,1,0],2  # -1
    input3 = [0,0,0,1,0,1,1,0], 3  # 3
    print(sol.minKBitFlips(*input1))
    print(sol.minKBitFlips(*input2))
    print(sol.minKBitFlips(*input3))
