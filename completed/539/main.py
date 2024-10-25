from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def hhmm_to_mins(self, t: str):
        hx, mx = t.split(':')
        return  int(hx) * 60 + int(mx)
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        max_time = 24 * 60
        res = max_time
        for i in range(len(timePoints)):
            x = self.hhmm_to_mins(timePoints[i])
            y = self.hhmm_to_mins(timePoints[i - 1])
            res = min(res, (y - x) % max_time, (x - y) % max_time)
        return res



if __name__ == '__main__':
    sol = Solution()
    input1 = ["23:59","00:00"]  # 1
    input2 = ["00:00","23:59","00:00"]  # 0
    input3 = ["00:00","12:00"]  # 720
    input4 = ["01:01","02:01"]  # 60
    input5 = ["12:12","00:13"]  # 719
    input6 = ["01:01","02:01","03:00"]  # 59
    print(sol.findMinDifference(input1))
    print(sol.findMinDifference(input2))
    print(sol.findMinDifference(input3))
    print(sol.findMinDifference(input4))
    print(sol.findMinDifference(input5))
    print(sol.findMinDifference(input6))
