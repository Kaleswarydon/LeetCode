from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.LinkedList import make_linked_list
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List

null = None


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        first_node = head
        second_node = head.next
        while second_node:
            if second_node:
                first_node.next = ListNode(gcd(first_node.val, second_node.val))
                first_node.next.next = second_node
            first_node = second_node
            second_node = second_node.next
        return head



if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([18,6,10,3])  # [18,6,6,2,10,1,3]
    input2 = make_linked_list([7])  # [7]
    print(sol.insertGreatestCommonDivisors(input1))
    print(sol.insertGreatestCommonDivisors(input2))
