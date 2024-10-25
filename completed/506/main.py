from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, score):
        medals = {"1": "Gold Medal", "2": "Silver Medal", "3": "Bronze Medal"}
        tmp = sorted([(x, i + 1) for i, x in enumerate(score)], key=lambda y: y[0], reverse=True)
        res = [0] * len(score)
        for j, z in enumerate(tmp):
            place = str(j + 1)
            res[z[1] - 1] = place if place not in medals else medals[place]
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [5,4,3,2,1]
    input2 = [10,3,8,9,4]
    print(sol.dummy(input1))
    print(sol.dummy(input2))
