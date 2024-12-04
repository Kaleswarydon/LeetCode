from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        res = float("inf")
        l = 0
        for r in range(len(nums)):
            for i, b in enumerate(bin(nums[r])[2:][::-1]):
                bits[i] += 1 if b == '1' else 0
                while int(''.join(['0' if not x else '1' for x in bits[::-1]]), 2) >= k:
                    res = min(res, r - l + 1)
                    print(l,r,r-l + 1)
                    if r > l:
                        for j, b2 in enumerate(bin(nums[l])[2:][::-1]):
                            bits[j] -= 1 if b2 == '1' else 0
                        l += 1
                    else:
                        break
        return -1 if res == float("inf") else res


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3], 2  # 1
    input2 = [2,1,8], 10  # 3
    input3 = [1,2], 0  # 1
    input4 = [1,2,32,21], 55  # 3
    print(sol.minimumSubarrayLength(*input1))
    print(sol.minimumSubarrayLength(*input2))
    print(sol.minimumSubarrayLength(*input3))
    print(sol.minimumSubarrayLength(*input4))
