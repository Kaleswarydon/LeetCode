from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        curr = 1
        res = [curr]
        for _ in range(n - 1):
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr == n or curr % 10 == 9:
                    curr //= 10
                curr += 1
            res.append(curr)
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = 13  # [1,10,11,12,13,2,3,4,5,6,7,8,9]
    input2 = 2  # [1,2]
    input3 = 100

    print(sol.lexicalOrder(input1))
    print(sol.lexicalOrder(input2))
    print(sol.lexicalOrder(input3))
