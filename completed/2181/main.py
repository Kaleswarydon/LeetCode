from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        interval_start = None
        interval_value = 0
        while current:
            if not current.val:
                current = current.next
                if interval_value:
                    interval_start.val = interval_value
                    interval_value = 0
                if interval_start:
                    interval_start.next = current
                interval_start = current
            else:
                interval_value += current.val
                current = current.next
        return head.next

if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([0,3,1,0,4,5,2,0])  # [4,11]
    input2 = make_linked_list([0,1,0,3,0,2,2,0])  # [1,3,4]
    print(sol.dummy(input1))
    print(sol.dummy(input2))
