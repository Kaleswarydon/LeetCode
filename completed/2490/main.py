from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        s = sentence.split()
        prev = s[0]
        for w in s[1:]:
            if prev[-1] != w[0]:
                return False
            prev = w
        return True


if __name__ == '__main__':
    sol = Solution()
    input1 = "leetcode exercises sound delightful"  # True
    input2 = "eetcode"  # True
    input3 = "Leetcode is cool"  # False
    print(sol.isCircularSentence(input1))
    print(sol.isCircularSentence(input2))
    print(sol.isCircularSentence(input3))
