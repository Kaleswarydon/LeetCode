from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, word, ch):
        occurrence = word.find(ch)
        if not occurrence < 0:
            return ''.join(list(reversed(word[:occurrence + 1]))) + word[occurrence + 1:]
        return word

if __name__ == '__main__':
    sol = Solution()
    input1 = "abcdefd", "d"
    input2 = "xyxzxe", "z"
    input3 = "abcd", "z"
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
