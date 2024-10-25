from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, node):
        while node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
                break
            node = node.next

if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([4,3])
    print(sol.dummy(input1))
    print(input1)
