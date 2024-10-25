from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minLength(self, s: str) -> int:
        stack: List[str] = []
        for c in s:
            if stack and ((stack[-1] == 'A' and c == 'B') or (stack[-1] == 'C' and c == 'D')):
                stack.pop()
                continue
            stack.append(c)
        return len(stack)

if __name__ == '__main__':
    sol = Solution()
    input1 = "ABFCACDB"  # 2
    input2 = "ACBBD"  # 5
    print(sol.minLength(input1))
    print(sol.minLength(input2))
