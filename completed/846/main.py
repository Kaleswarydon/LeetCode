from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from typing import List


class Solution:
    def dummy(self, hand: List[int], groupSize: int):
        if len(hand) % groupSize:
            return False
        ht = defaultdict(lambda: 0)
        for c in hand:
            ht[c] += 1
        card_vals = sorted(ht)
        while card_vals:
            if ht.get(card_vals[-1]):
                for i in range(groupSize):
                    ht[card_vals[-1] - i] -= 1
                    if ht.get(card_vals[-1] - i) == -1:
                        return False
            else:
                card_vals.pop()
        return True





if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3,6,2,3,4,7,8], 3
    input2 = [1,2,3,4,5], 4
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
