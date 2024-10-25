from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, head: Optional[ListNode]) -> List[int]:
        current = head
        extrema = []
        prev_prev = None
        prev = None
        ind = -1
        while current:
            if prev_prev is not None and prev is not None and current is not None:
                if prev_prev.val < prev.val > current.val or prev_prev.val > prev.val < current.val:
                    extrema.append(ind)
            prev_prev = prev
            prev = current
            current = current.next
            ind += 1
        try:
            max_distance = extrema[-1] - extrema[0]
            min_distance = min([y - x for x, y in zip(extrema, extrema[1:])])
        except:
            return [-1,-1]
        return [min_distance, max_distance]

if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([3,1])  # [-1,-1]
    input2 = make_linked_list([5,3,1,2,5,1,2])  # [1,3]
    input3 = make_linked_list([1,3,2,2,3,2,2,2,7])  # [3,3]
    input4 = make_linked_list([5,3,1,2])
    input5 = make_linked_list([6,8,4,1,9,6,6,10,6])  # [1,6]
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
    print(sol.dummy(input5))
