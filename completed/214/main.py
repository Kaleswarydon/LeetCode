from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s
        ht = set()
        longest = 0
        for i in range(len(s)):
            ht.add(hash(s[:i]))
            h_rev = hash(s[:i][::-1])
            if h_rev in ht:
                longest = i
        return s[longest:][::-1] + s

if __name__ == '__main__':
    sol = Solution()
    input1 = "aacecaaa"  # "aaacecaaa"
    input2 = "abcd"  # "dcbabcd"
    input3 = "aabba"  # "abbaabba"
    input4 = "adcba"  # "abcdadcba"
    input5 = "aa"  # "aa"
    input6 = "ab"  # "aa"
    input7 = "ababbbabbaba"  # "ababbabbbababbbabbaba"
    print(sol.shortestPalindrome(input1))
    print(sol.shortestPalindrome(input2))
    print(sol.shortestPalindrome(input3))
    print(sol.shortestPalindrome(input4))
    print(sol.shortestPalindrome(input5))
    print(sol.shortestPalindrome(input6))
    print(sol.shortestPalindrome(input7))
