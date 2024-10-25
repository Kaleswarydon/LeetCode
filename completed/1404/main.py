from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, s):
        if len(s) == 1:
            return int(not int(s))
        rev_s = deque(s[::-1])
        cntr = 0
        while len(rev_s) > 1:
            if rev_s[0] == "0":
                rev_s.popleft()
            else:
                try:
                    tmp_ind = rev_s.index("0")
                except:
                    rev_s.append("0")
                    tmp_ind = len(rev_s) - 1
                for i in range(tmp_ind):
                    rev_s[i] = "0"
                rev_s[tmp_ind] = "1"
            cntr += 1
        return cntr

if __name__ == '__main__':
    sol = Solution()
    input1 = "1101"
    input2 = "10"
    input3 = "1"
    input4 = "0"
    input5 = "11000"
    input6 = "110"
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
    print(sol.dummy(input5))
    print(sol.dummy(input6))
