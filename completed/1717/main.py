from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # remove ab from string: x points
        # remove ba from string: y points
        # goal: max points
        res = 0
        matchers = sorted([(x, "ab"), (y, "ba")], key=lambda z: z[0], reverse=True)
        altered = True
        while altered:
            for score, match in matchers:
                tmp = s.split(match)
                res += (len(tmp) - 1) * score
                s = ''.join(tmp)
                if len(tmp) - 1:
                    altered = True
                    break
                altered = False
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "cdbcbbaaabab", 4, 5  # 19
    input2 = "aabbaaxybbaabb", 5, 4  # 20
    print(sol.maximumGain(*input1))
    print(sol.maximumGain(*input2))
