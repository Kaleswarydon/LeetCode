from icecream import ic as print
from collections import defaultdict
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

def reverse_ll(head):
    if not head:
        return None
    if not head.next:
        return head
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

def get_len(ll: Optional[ListNode]) -> int:
    l = 1
    current = ll
    if not current:
        return 0
    while True:
        if not current or not current.next:
            break
        l += 1
        current = current.next
    return l

class Solution:
    def isPalindrome(self, head):
        list_len = get_len(head)
        half_len = list_len // 2
        current = head
        for i in range(half_len):
            current = current.next
        second_half = reverse_ll(current)
        current1 = head
        current2 = second_half
        while True:
            try:
                if current1.val != current2.val:
                    return False
            except:
                return True
            current1 = current1.next
            current2 = current2.next



if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([1,2,2,1])
    input2 = make_linked_list([1,2])
    input3 = make_linked_list([1,2,3,2,1])
    input4 = make_linked_list([1,1])
    input5 = make_linked_list([1])
    print(sol.isPalindrome(input1))
    print(sol.isPalindrome(input2))
    print(sol.isPalindrome(input3))
    print(sol.isPalindrome(input4))
    print(sol.isPalindrome(input5))
