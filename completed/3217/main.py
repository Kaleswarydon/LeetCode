from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        tmp = []
        current = self
        while current:
            tmp.append(current.val)
            current = current.next
        return "[" + ', '.join([str(x) for x in tmp]) + "]"

    def __repr__(self):
        tmp = []
        current = self
        while current:
            tmp.append(current.val)
            current = current.next
        return "[" + ', '.join([str(x) for x in tmp]) + "]"

def make_linked_list(l: list):
    head = ListNode(l[0])
    current = head
    for x in l[1:]:
        current.next = ListNode(x)
        current = current.next
    return head


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        def delete_values_from_ll(head: Optional[ListNode], values: List[int]):
            values = set(values)
            prev = None
            current = head
            while current:
                changed = False
                if current.val in values:
                    if current == head:
                        head = current.next
                    if prev:
                        changed = True
                        prev.next = current.next
                if not changed:
                    prev = current
                current = current.next
            return head
        return delete_values_from_ll(head, nums)


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,3], make_linked_list([1,2,3,4,5])  # [4,5]
    input2 = [1], make_linked_list([1,2,1,2,1,2])  # [2,2,2]
    input3 = [5], make_linked_list([1,2,3,4])  # [1,2,3,4]
    input4 = [1,7,6,2,4], make_linked_list([3,7,1,8,1])  # [3,8]
    print(sol.modifiedList(*input1))
    print(sol.modifiedList(*input2))
    print(sol.modifiedList(*input3))
    print(sol.modifiedList(*input4))
