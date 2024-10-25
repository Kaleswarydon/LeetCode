from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        def find_fix(s1, s2):
            res = 0
            for i in range(len(s2)):
                if s1[i] == s2[i]:
                    res += 1
                else:
                    break
            return res
        x = sentence1.split()
        y = sentence2.split()
        if len(y) > len(x):
            x, y = y, x
        prefix = find_fix(x, y)
        postfix = find_fix(x[::-1], y[::-1])
        return prefix + postfix >= len(y)
if __name__ == '__main__':
    sol = Solution()
    input1 = "My name is Haley", "My Haley"  # True
    input2 = "of", "A lot of words"  # False
    input3 = "Eating right now", "Eating"  # True
    input4 = "a x A y A", "a A"  # True
    input5 = "Ogn WtWj HneS", "Ogn WtWj HneS"  # True
    print(sol.areSentencesSimilar(*input1))
    print(sol.areSentencesSimilar(*input2))
    print(sol.areSentencesSimilar(*input3))
    print(sol.areSentencesSimilar(*input4))
    print(sol.areSentencesSimilar(*input5))
