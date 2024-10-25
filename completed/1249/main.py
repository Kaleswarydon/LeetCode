from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def helper(self, s_list, reverse=False):
        open_par = 0
        close_par = 0
        del_indices = []
        for i, c in enumerate(s_list):
            if c == "(":
                open_par += 1
            if c == ")":
                close_par += 1
            if reverse:
                if close_par < open_par:
                    del_indices.append(i)
                    open_par -= 1
            else:
                if close_par > open_par:
                    del_indices.append(i)
                    close_par -= 1
        for d in del_indices[::-1]:
            del s_list[d]
        return s_list


    def minRemoveToMakeValid(self, s):
        s_list = list(s)
        s_list = self.helper(s_list)
        s_list = self.helper(s_list[::-1], reverse=True)
        return s_list[::-1]

if __name__ == '__main__':
    sol = Solution()
    input1 = "lee(t(c)o)de)"
    input2 = "a)b(c)d"
    input3 = "))(("
    print(sol.minRemoveToMakeValid(input1))
    print(sol.minRemoveToMakeValid(input2))
    print(sol.minRemoveToMakeValid(input3))
