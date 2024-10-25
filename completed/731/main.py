from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class MyCalendarTwo:
    def __init__(self):
        self.singly_booked = []
        self.doubly_booked = []
    def book(self, start: int, end: int) -> bool:
        #print(start, end, self.doubly_booked)
        for s0, e0 in self.doubly_booked:
            if start <= s0 < end or s0 <= start < e0:
                #print(s0,e0, start, end)
                return False
        for s1, e1 in self.singly_booked:
            x, y = -1, -1
            if start <= s1 < end or s1 <= start < e1:
                x = max(start, s1)
                y = min(end, e1)
            if x != -1 and y != -1:
                #print(x, y, s1, e1, start, end)
                self.doubly_booked.append((x, y))
        self.singly_booked.append((start, end))
        return True

if __name__ == '__main__':#
    def helper(inp):
        sol = MyCalendarTwo()
        res = []
        for i in inp:
            if not i or len(i) != 2 or i == [None, None]:
                res.append(None)
            else:
                res.append(sol.book(*i))
        return res

    input1 = [[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]  # [null, true, true, true, false, true, true]
    input2 = [[],[89,100],[30,43],[92,100],[31,49],[59,76],[60,73],[31,49],[80,99],[48,60],[36,52],[67,82],[96,100],[22,35],[18,32],[9,24],[11,27],[94,100],[12,22],[61,74],[3,20],[14,28],[27,37],[5,20],[1,11],[96,100],[33,44],[90,100],[40,54],[23,35],[18,32],[78,89],[56,66],[83,93],[45,59],[40,59],[94,100],[99,100],[86,96],[43,61],[29,45],[21,36],[13,31],[17,30],[16,30],[80,94],[38,50],[15,30],[62,79],[25,39],[73,85],[39,56],[80,97],[42,57],[32,47],[59,78],[35,53],[56,74],[75,85],[39,54],[63,82]]
    print(helper(input1))
    print(helper(input2))
