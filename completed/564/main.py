from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List
import math

null = None


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def is_number(s):
            try:
                return int(s)
            except:
                return False
        def is_palindrome(pa):
            if not is_number(pa):
                return False
            pa = str(pa)
            tmp1 = pa[:len(pa) // 2]
            if len(pa) == 2:
                tmp2 = pa[-1]
            elif len(pa) % 2:
                tmp2 = pa[(len(pa) // 2) + 1:][::-1]
            else:
                tmp2 = pa[(len(pa) // 2):][::-1]
            if len(pa) == 1 or tmp1 == tmp2:
                return int(pa)
            return False
        if len(n) == 1:
            return str(int(n) - 1)
        m = math.ceil((len(n)-1) / 2)
        prefix = n[:m]
        middle = n[m]
        postfix = n[:m][::-1]
        candidates = [prefix + middle + postfix,
                      prefix + postfix,
                      prefix + str(int(middle) - 1) + postfix,
                      prefix + str(int(middle) + 1) + postfix,
                      str(int(prefix) - 1) + str(int(prefix) - 1)[::-1],
                      str(int(prefix) + 1) + str(int(prefix) + 1)[::-1],
                      str(int(prefix) - 2) + str(int(prefix) - 2)[::-1],
                      str(int(prefix) + 2) + str(int(prefix) + 2)[::-1],
                      str(int(prefix) + 2) + str(int(prefix) + 2)[::-1],
                      str(int(n) + 1),
                      str(int(n) + 2),
                      str(int(n) - 1),
                      str(int(n) - 2)]
        #print(candidates)
        res = []
        for c in candidates:
            if is_palindrome(c) and c != n:
                try:
                    heapq.heappush(res, (abs(int(c) - int(n)), int(c)))
                except:
                    pass
        #print(res)
        return str(res[0][1])


if __name__ == '__main__':
    sol = Solution()
    input1 = "123"  # "121"
    input2 = "1"  # "0"
    input3 = "12320"  # "12321"
    input4 = "1220"  # "1221"
    input5 = "99800"  # "99799"
    input6 = "999999999999999999"  # "10...01"
    input7 = "11"  # "9"
    input8 = "101"
    input9 = "1000000000000000"
    input10 = "1837722381"
    input11 = "1805170081"
    print(sol.nearestPalindromic(input1))
    print(sol.nearestPalindromic(input2))
    print(sol.nearestPalindromic(input3))
    print(sol.nearestPalindromic(input4))
    print(sol.nearestPalindromic(input5))
    print(sol.nearestPalindromic(input6))
    print(sol.nearestPalindromic(input7))
    print(sol.nearestPalindromic(input8))
    print(sol.nearestPalindromic(input9))
    print(sol.nearestPalindromic(input10))
    print(sol.nearestPalindromic(input11))
