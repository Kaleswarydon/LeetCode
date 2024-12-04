from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def check_strictly_increasing(l):
            for i in range(1, len(l)):
                if l[i] <= l[i-1]:
                    return False
            return True
        if check_strictly_increasing(nums):
            return True
        import re
        prime = lambda x: not re.match(r'^.?$|^(..+?)\1+$', '1' * x)
        nums = [0] + nums
        #primes = [z for z in range(2, 1001) if prime(z)]
        for j in range(1, len(nums)):
            g = (nums[j] - nums[j-1])
            if g > 0:
                for u in range(g, -1, -1):
                    if prime(u) and nums[j] - u > nums[j-1]:
                        nums[j] -= u
                        break
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    input1 = [4,9,6,10]  # True
    input2 = [6,8,11,12]  # True
    input3 = [5,8,3]  # False
    print(sol.primeSubOperation(input1))
    print(sol.primeSubOperation(input2))
    print(sol.primeSubOperation(input3))
