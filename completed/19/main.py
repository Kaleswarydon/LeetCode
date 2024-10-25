from typing import Optional

#from icecream import ic as print


def make_linked_list(l: list):
    head = ListNode(l[0])
    current = head
    for x in l[1:]:
        current.next = ListNode(x)
        current = current.next
    return head


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


class Solution:
    def get_len(self, ll: Optional[ListNode]) -> int:
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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.get_len(head)
        if not l - n:
            return head.next
        prev = None
        current = head
        cntr = 0
        while current:
            if cntr == l - n and prev:
                prev.next = current.next
            else:
                prev = current
            current = current.next
            cntr += 1
        return head

if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([1,2,3,4,5])
    input2 = make_linked_list([1])
    input3 = make_linked_list([1,2])
    input4 = make_linked_list([1,2])
    print(sol.removeNthFromEnd(input1, 2))
    print(sol.removeNthFromEnd(input2, 1))
    print(sol.removeNthFromEnd(input3, 1))
    print(sol.removeNthFromEnd(input4, 2))
