from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        if not k:
            return res
        if k > 0:
            start, stop = 0, len(code)
            step = 1
            curr_interval = code[:k+1]
            curr_sum = sum(curr_interval)
        else:
            stop, start = -1, len(code) - 1
            step = -1
            curr_interval = code[len(code)+k-1:]
            curr_sum = sum(curr_interval)
        #print(curr_sum, len(code)+k, curr_interval)
        for i in range(start, stop, step):
            curr_sum -= code[i]
            res[i] = curr_sum
            curr_sum += code[(k+i+step)%len(code)]
            #print(i, curr_sum, res[i], code[i], code[(k+i+step) % len(code)])
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [5,7,1,4], 3  # [12,10,16,13]
    input2 = [1,2,3,4], 0  # [0,0,0,0]
    input3 = [2,4,9,3], -2  # [12,5,6,13]
    input4 = [10,5,7,7,3,2,10,3,6,9,1,6], -4  # [22,26,22,28,29,22,19,22,18,21,28,19]
    print(sol.decrypt(*input1))
    print(sol.decrypt(*input2))
    print(sol.decrypt(*input3))
    print(sol.decrypt(*input4))
