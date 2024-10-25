from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val

if __name__ == '__main__':
    def helper(inp):
        res = [None]
        sol = CustomStack(*inp[1][0])
        for i in range(1, len(inp[0])):
            func = getattr(sol, inp[0][i])
            r = func(*inp[1][i])
            res.append(r)
        return res
    input1 = [["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"], [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]]  # [null,null,null,2,null,null,null,null,null,103,202,201,-1]
    print(helper(input1))

