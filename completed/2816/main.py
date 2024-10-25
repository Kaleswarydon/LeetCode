from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def read_num(self, node):
        res = ""
        while node:
            res += str(node.val)
            node = node.next
        return res

    def doubleIt(self, head):
        head = reverse_ll(head)
        node = head
        carry = 0
        while node:
            tmp = str((node.val * 2) + carry)
            if len(tmp) > 1:
                tmp = tmp[1]
                carry = 1
            else:
                carry = 0
            node.val = int(tmp)
            if carry and not node.next:
                node.next = ListNode()
            node = node.next
        return reverse_ll(head)

if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([1,8,9])
    input2 = make_linked_list([9,9,9])
    print(sol.doubleIt(input1))
    print(sol.doubleIt(input2))
