from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class AllOne:
    def __init__(self):
        self.str_to_count = defaultdict(lambda: 0)
        self.count_to_str = defaultdict(lambda: set())
        self.max_cnt = float("-inf")
        self.min_cnt = float("inf")

    def inc(self, key: str) -> None:
        cnt = self.str_to_count[key]
        try:
            self.count_to_str[cnt].remove(key)
            if not len(self.count_to_str[cnt]):
                del self.count_to_str[cnt]
        except:
            pass
        if not len(self.count_to_str[self.min_cnt]):
            del self.count_to_str[self.min_cnt]
            self.min_cnt = cnt + 1
        else:
            self.min_cnt = min(self.min_cnt, cnt + 1)
        self.str_to_count[key] += 1
        self.max_cnt = max(self.max_cnt, cnt + 1)
        self.count_to_str[cnt + 1].add(key)

    def dec(self, key: str) -> None:
        cnt = self.str_to_count[key]
        try:
            self.count_to_str[cnt].remove(key)
            if not len(self.count_to_str[cnt]):
                del self.count_to_str[cnt]
        except:
            pass
        if not len(self.count_to_str[self.max_cnt]):
            self.max_cnt = cnt - 1
        else:
            self.max_cnt = max(self.max_cnt, cnt - 1)
        self.str_to_count[key] -= 1
        if not self.min_cnt:
            del self.str_to_count[key]
        self.min_cnt = min(self.min_cnt, cnt - 1)
        self.count_to_str[cnt - 1].add(key)
        if not self.min_cnt:
            del self.count_to_str[0]
            self.min_cnt = min(self.count_to_str.keys())

    def getMaxKey(self) -> str:
        for x in self.count_to_str[self.max_cnt]:
            return x
        return ""

    def getMinKey(self) -> str:
        for x in self.count_to_str[self.min_cnt]:
            return x
        return ""

if __name__ == '__main__':
    def helper(inp):
        sol = AllOne()
        res = [None]
        for i in range(1, len(inp[0])):
            func = getattr(sol, inp[0][i])
            r = func(*inp[1][i])
            #print(inp[0][i], inp[1][i], sol.str_to_count, sol.count_to_str, sol.max_cnt, sol.min_cnt)
            res.append(r)
        return res
    input1 = [["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"], [[],["hello"],["hello"],[],[],["leet"],[],[]]]  # [null, null, null, "hello", "hello", null, "hello", "leet"]
    input2 = [["AllOne","getMaxKey","getMinKey"], [[],[],[]]]  # [null,"",""]
    input3 = [["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"], [[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]]  # [null,null,null,null,null,null,null,null,null,"a",null,"c","c"]
    print(helper(input1))
    print(helper(input2))
    print(helper(input3))
