from icecream import ic as print
from collections import defaultdict, deque
from functools import reduce
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def fractionAddition(self, expression: str) -> str:
        e = list(expression)
        u = []
        v = []
        tmp = []
        int_added = False
        for i, p in enumerate(reversed(e)):
            try:
                t = int(p)
                if int_added:
                    t = int(str(t) + str(tmp.pop()))
                tmp.append(t)
                int_added = True
            except:
                if p == '-':
                    tmp[-1] *= -1
                int_added = False
        for j in range(len(tmp) - 1, -1, -1):
            if j % 2:
                u.append(tmp[j])
            else:
                v.append(tmp[j])
        base = reduce(lambda x, y: x * y, set(v), 1)
        for k in range(len(u)):
            u[k] *= base // v[k]
        res_u = sum(u)
        res_v = base
        d = res_v
        while d >= 2:
            if not res_u % d and not res_v % d:
                res_u //= d
                res_v //= d
                d = res_v
                continue
            d -= 1
        if not res_v:
            res_v = 1
        return str(res_u) + '/' + str(res_v)




if __name__ == '__main__':
    sol = Solution()
    input1 = "-1/2+1/2"  # "0/1
    input2 = "-1/2+1/2+1/3"  # "1/3"
    input3 = "1/3-1/2"  # "-1/6"
    input4 = "-5/2+10/3+7/9"  # "29/18"
    input5 = "7/3+5/2-3/10"  # "68/15
    print(sol.fractionAddition(input1))
    print(sol.fractionAddition(input2))
    print(sol.fractionAddition(input3))
    print(sol.fractionAddition(input4))
    print(sol.fractionAddition(input5))
