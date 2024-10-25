from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo = defaultdict(float)
        def helper(i):
            if i == len(books):
                return 0
            if memo[i]:
                return memo[i]
            memo[i] = float("inf")
            books_width = 0
            books_height = 0
            for j in range(i, len(books)):
                w, h = books[j]
                if books_width + w > shelfWidth:
                    break
                books_width += w
                books_height = max(books_height, h)
                memo[i] = min(memo[i], helper(j + 1) + books_height)
            return memo[i]
        return helper(0)


if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4  # 6
    input2 = [[1,3],[2,4],[3,2]], 6  # 4
    print(sol.minHeightShelves(*input1))
    print(sol.minHeightShelves(*input2))
