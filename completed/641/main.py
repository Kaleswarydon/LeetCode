from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.q: List[any] = [None for _ in range(k)]
        self.max_len: int = k
        self.current_len = 0
        self.front: int = 0
        self.back: int = 0

    def move_ptr(self, current_index: int, direction: str) -> int:
        if direction == "forward":
            return (current_index + 1) % self.max_len
        else:  # direction == "backwards"
            return (current_index - 1) % self.max_len

    def insertFront(self, value: int) -> bool:
        new_index = self.front
        br = False
        while self.q[new_index] is not None:
            if br:
                break
            new_index = self.move_ptr(new_index, "backwards")
            if new_index == self.back:
                br = True
        if self.q[new_index] is None:
            self.q[new_index] = value
            self.front = new_index
            self.current_len += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        new_index = self.back
        br = False
        while self.q[new_index] is not None:
            if br:
                break
            new_index = self.move_ptr(new_index, "forward")
            if new_index == self.front:
                br = True
        if self.q[new_index] is None:
            self.q[new_index] = value
            self.back = new_index
            self.current_len += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.q[self.front] is not None:
            self.q[self.front] = None
            new_index = self.move_ptr(self.front, "forward")
            if self.q[new_index] is not None:
                self.front = new_index
            self.current_len -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.q[self.back] is not None:
            self.q[self.back] = None
            new_index = self.move_ptr(self.back, "backwards")
            if self.q[new_index] is not None:
                self.back = new_index
            self.current_len -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.q[self.front] is not None:
            return self.q[self.front]
        return -1

    def getRear(self) -> int:
        if self.q[self.back] is not None:
            return self.q[self.back]
        return -1

    def isEmpty(self) -> bool:
        return self.current_len == 0

    def isFull(self) -> bool:
        return self.current_len == self.max_len



if __name__ == '__main__':
    def helper(inp):
        res = []
        sol = MyCircularDeque(*inp[1][0])
        for i in range(1, len(inp[0])):
            func = getattr(sol, inp[0][i])
            r = func(*inp[1][i])
            print(sol.q, sol.front, sol.back, inp[0][i], *inp[1][i], r)
            res.append(r)
        return res
    input1 = [["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"], [[3],[1],[2],[3],[4],[],[],[],[4],[]]]
    input2 = [["MyCircularDeque","insertFront","getFront","isEmpty","deleteFront","insertLast","getRear","insertLast","insertFront","deleteLast","insertLast","isEmpty"], [[8],[5],[],[],[],[3],[],[7],[7],[],[4],[]]]
    input3 = [["MyCircularDeque","insertFront","deleteLast","getRear","getFront","getFront","deleteFront","insertFront","insertLast","insertFront","getFront","insertFront"], [[4],[9],[],[],[],[],[],[6],[5],[9],[],[6]]]
    #print(helper(input1))
    #print(helper(input2))
    print(helper(input3))