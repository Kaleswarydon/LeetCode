from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, s):
        open_parentheses = []
        intervals = []
        for i in range(len(s)):
            if s[i] == '(':
                open_parentheses.append(i)
            if s[i] == ')':
                open_par_ind = open_parentheses.pop()
                heapq.heappush(intervals, (-len(open_parentheses), open_par_ind, i))
        while intervals:
            rank, interval_start, interval_end = heapq.heappop(intervals)
            s = s[:interval_start+1] + s[interval_start+1:interval_end][::-1] + s[interval_end:]
        return s.replace('(', '').replace(')', '')

if __name__ == '__main__':
    sol = Solution()
    input1 = "(abcd)"  # "dcba"
    input2 = "(u(love)i)"  # "iloveu"
    input3 = "(ed(et(oc))el)"  # "leetcode"
    input4 = "sxmdll(q)eki(x)"  # "sxmdllqekix"
    input5 = "(sxmdll(q)eki(x))"
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
    print(sol.dummy(input5))
