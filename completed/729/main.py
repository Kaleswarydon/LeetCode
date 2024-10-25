from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class MyCalendar:
    def __init__(self):
        self.state = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.state:
            if start <= s < end or s <= start < e:
                return False
        self.state.append((start, end))
        return True

if __name__ == '__main__':#
    def helper(inp):
        res = []
        for i in inp:
            if not i or len(i) != 2 or i == [None, None]:
                res.append(None)
            else:
                res.append(sol.book(*i))
        return res
    sol = MyCalendar()
    input1 = [[], [10, 20], [15, 25], [20, 30]]  # [null, true, false, true]
    print(helper(input1))
