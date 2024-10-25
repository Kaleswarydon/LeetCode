from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for p in s:
            if p == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(p)
        return len(stack)


if __name__ == '__main__':
    sol = Solution()
    input1 = "())"  # 1
    input2 = "((("  # 3
    print(sol.minAddToMakeValid(input1))
    print(sol.minAddToMakeValid(input2))
