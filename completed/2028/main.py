from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        n_s = ((len(rolls) + n) * mean) - sum(rolls)
        if n_s < n or n_s < 0 or n_s > n * 6:
            return []
        di, mo = divmod(n_s, n)
        return [di + int(i < mo) for i in range(n)]



if __name__ == '__main__':
    sol = Solution()
    input1 = [3,2,4,3], 4, 2  # [6,6]
    input2 = [1,5,6], 3, 4  # [2,3,2,2]
    input3 = [1,2,3,4], 6, 4  # []
    input4 = [6,3,4,3,5,3], 1, 6  # []
    input5 = [4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3], 2, 53
    print(sol.missingRolls(*input1))
    print(sol.missingRolls(*input2))
    print(sol.missingRolls(*input3))
    print(sol.missingRolls(*input4))
    print(sol.missingRolls(*input5))
