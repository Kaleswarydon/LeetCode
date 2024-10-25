from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        r = skill[0] + skill[-1]
        res = 0
        for i in range(len(skill) // 2):
            t = skill[i] + skill[len(skill) - 1 - i]
            if t != r:
                return -1
            res += skill[i] * skill[len(skill) - 1 - i]
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [3,2,5,1,3,4]  # 22
    input2 = [3,4]  # 12
    input3 = [1,1,2,3]  # -1
    print(sol.dividePlayers(input1))
    print(sol.dividePlayers(input2))
    print(sol.dividePlayers(input3))
