from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arriving = []
        for i, f in enumerate(times):
            heapq.heappush(arriving, (*f, i))
        free_chairs = [0]
        leaving = []
        while arriving:
            current = heapq.heappop(arriving)
            #print(current)
            while leaving and leaving[0][0] <= current[0]:
                #print(leaving[0][-2], "freeing chair:", leaving[0][-1])
                tmp = heapq.heappop(leaving)
                heapq.heappush(free_chairs, tmp[-1])
            if free_chairs:
                chair = heapq.heappop(free_chairs)
            else:
                chair = len(leaving)
            if current[-1] == targetFriend:
                return chair
            #print(current[-1], "occupying chair:", chair)
            heapq.heappush(leaving, (*current[1:], chair))



if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,4],[2,3],[4,6]], 1  # 1
    input2 = [[3,10],[1,5],[2,6]], 0  # 2
    input3 = [[1,2],[2,10],[3,10],[4,10],[5,10],[6,10],[7,10],[8,10],[9,10],[10,11]], 8  # 7
    input4 = [[1,2],[2,3]], 1  # 0
    input5 = [[4,5],[6,8],[8,10],[1,8]], 2  # 0
    input6 = [[33,35],[26,29],[9,28],[4,31],[8,10],[32,34],[15,24],[27,39],[14,36],[1,14],[25,39],[5,27],[6,15],[2,38],[19,36],[24,34],[3,26]], 0  # 3
    input7 = [[2,4],[4,9],[3,4],[6,8],[5,10]], 4  # 1
    print(sol.smallestChair(*input1))
    print(sol.smallestChair(*input2))
    print(sol.smallestChair(*input3))
    print(sol.smallestChair(*input4))
    print(sol.smallestChair(*input5))
    print(sol.smallestChair(*input6))
    print(sol.smallestChair(*input7))
