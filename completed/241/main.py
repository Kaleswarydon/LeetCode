from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):
            if expression[i] in self.ops:
                for t1 in self.diffWaysToCompute(expression[:i]):
                    for t2 in self.diffWaysToCompute(expression[i+1:]):
                        res.append(self.ops[expression[i]](t1, t2))
        if not res:
            res = [int(expression)]
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "2-1-1"  # [0,2]
    input2 = "2*3-4*5"  # [-34,-14,-10,-10,10]
    print(sol.diffWaysToCompute(input1))
    print(sol.diffWaysToCompute(input2))
