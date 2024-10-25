from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, head):
        middle_node, middle_ind = get_middle(head)
        ll1, ll2 = split_at(head, middle_ind)
        ll2 = reverse_ll(ll2)
        current1 = ll1
        current2 = ll2
        while current1 or current2:
            try:
                c1_next = current1.next
                c2_next = current2.next
                current1.next = current2
                current1 = current1.next
                current1.next = c1_next
                current1 = current1.next
                current2 = c2_next
            except:
                break
        return ll1


if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([1,2,3,4])
    input2 = make_linked_list([1,2,3,4,5])
    print(sol.dummy(input1))
    print(sol.dummy(input2))
