from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap(l, i1,i2):
            tmp = l[i1]
            l[i1] = l[i2]
            l[i2] = tmp
            return l
        inp = "".join([str(x) for y in board for x in y])
        if inp == "123450":
            return 0
        poss_dirs = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}
        q = deque([(1, inp)])
        visited = set()
        while q:
            cntr, curr = q.pop()
            curr_zero_ind = curr.find('0')
            for next_zero_pos in poss_dirs.get(curr_zero_ind):
                c = "".join(swap(list(curr), next_zero_pos, curr_zero_ind))
                if c == "123450":
                    return cntr
                if not c in visited:
                    q.appendleft((cntr + 1, c))
                    visited.add(c)
        return -1




if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,2,3],[4,0,5]]  # 1
    input2 = [[1,2,3],[5,4,0]]  # -1
    input3 = [[4,1,2],[5,0,3]]  # 5
    print(sol.slidingPuzzle(input1))
    print(sol.slidingPuzzle(input2))
    print(sol.slidingPuzzle(input3))
