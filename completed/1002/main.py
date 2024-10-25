from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, words):
        res = None
        for x in words:
            tmp = [0] * 26
            for y in x:
                tmp[ord(y) - 97] += 1
            if res is None:
                res = tmp
            else:
                for i in range(26):
                    res[i] = min(res[i], tmp[i])
        ret = []
        for j, c in enumerate(res):
            for k in range(c):
                ret.append(chr(j + 97) )
        return ret


if __name__ == '__main__':
    sol = Solution()
    input1 = ["bella","label","roller"] # ["e","l","l"]
    input2 = ["cool","lock","cook"] # ["c","o"]
    input3 = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"] # []
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))