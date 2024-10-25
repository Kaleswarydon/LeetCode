from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def fill_hist(s):
            for x in s.split(' '):
                if not hist[x]:
                    hist[x] = 1
                else:
                    hist[x] = -1
        hist = defaultdict(int)
        fill_hist(s1)
        fill_hist(s2)
        return [y for y in hist if hist[y] == 1]


if __name__ == '__main__':
    sol = Solution()
    input1 = "this apple is sweet", "this apple is sour"  # ["sweet","sour"]
    input2 = "apple apple", "banana"  # ["banana"]
    print(sol.uncommonFromSentences(*input1))
    print(sol.uncommonFromSentences(*input2))
