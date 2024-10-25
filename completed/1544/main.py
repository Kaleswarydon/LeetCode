from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def is_bad(self, a: str, b: str):
        return ((a.isupper() and b.islower()) or (a.islower() and b.isupper())) and a.lower() == b.lower()

    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s
        s_list = list(s)
        s_list_old_len = 0
        while s_list and s_list_old_len != len(s_list):
            remove_indices = []
            for i in range(len(s_list) - 1):
                a = s_list[i]
                b = s_list[i + 1]
                if self.is_bad(a, b) and i not in remove_indices:
                    remove_indices.extend([i, i+1])
            s_list_old_len = len(s_list)
            for j in remove_indices[::-1]:
                del s_list[j]
        return ''.join(s_list)

if __name__ == '__main__':
    sol = Solution()
    input1 = "leEeetcode"
    input2 = "abBAcC"
    input3 = "s"
    print(sol.makeGood(input1))
    print(sol.makeGood(input2))
    print(sol.makeGood(input3))
