from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *

class Solution:
    def dummy(self, head):
        if not head:
            return None
        prev = head
        current = head.next
        head.next = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            if not tmp:
                break
            current = tmp
        return current

if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([1,2,3,4,5])
    print(sol.dummy(input1))
