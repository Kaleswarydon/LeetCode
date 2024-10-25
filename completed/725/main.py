from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.LinkedList import make_linked_list
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None

def get_len(head: Optional[ListNode]) -> int:
    l = 1
    current = head
    if not current:
        return 0
    while True:
        if not current or not current.next:
            break
        l += 1
        current = current.next
    return l

def split_at(head: Optional[ListNode], ind: int) -> (Optional[ListNode], Optional[ListNode]):
    assert ind >= 0
    current = head
    prev = None
    cntr = 0
    while current and cntr <= ind:
        prev = current
        current = current.next
        cntr += 1
    prev.next = None
    return head, current

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = get_len(head)
        d, m = divmod(l, k)
        res = []
        current = head
        while k:
            try:
                x, y = split_at(current, d - 1  + int(m > 0))
                res.append(x)
                current = y
            except:
                res.append(ListNode("", None))
            m -= 1
            k -= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([1,2,3]), 5
    input2 = make_linked_list([1,2,3,4,5,6,7,8,9,10]), 3
    print(sol.splitListToParts(*input1))
    print(sol.splitListToParts(*input2))
