from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        student_round = sum(chalk)
        k %= student_round
        for i, s in enumerate(chalk):
            if k < s:
                return i
            k -= s


if __name__ == '__main__':
    sol = Solution()
    input1 = [5,1,5], 22  # 0
    input2 = [3,4,1,2], 25  # 1
    print(sol.chalkReplacer(*input1))
    print(sol.chalkReplacer(*input2))
