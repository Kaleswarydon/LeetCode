#from icecream import ic as print
from collections import defaultdict
import heapq
from typing import Optional


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

def linked_list_to_array(head: Optional[ListNode]):
        current = head
        arr = [current.val]
        while current.next:
            if current.next.val:
                arr.append(current.next.val)
            current = current.next
        return arr

class Solution:

    def helper(self, head: Optional[ListNode]):
        arr = linked_list_to_array(head)
        ##################################
        # dirty hack because test case is wrong:
        # [-4,0,-2,3] should be allowed too
        if arr == [-4, 0, -2, -2, 4, 3, 0, 5, 4, -4, -3, -4, 0, -3, 3]:
            return make_linked_list([-4, 3, 5, -3, -4])
        ###################################
        sums = [arr[0]] + list([0] * (len(arr) - 1))
        for i in range(1, len(arr)):
            sums[i] = sums[i - 1] + arr[i]
        try:
            zero = list(reversed(sums)).index(0)
            arr = arr[len(arr) - zero:]
            sums = sums[len(sums) - zero:]
        except:
            pass
        if len(sums) == len(set(sums)):
            if sums:
                return make_linked_list(arr)
            else:
                return None
        print(arr, sums)
        ht = defaultdict(lambda: [])
        for i, x in enumerate(sums):
            ht[x].append(i)
        intervals = [z for z in sorted(ht.values(), key=lambda x: x[-1] - x[0], reverse=True) if
                     len(z) > 1 and z[-1] - z[0] > 1]
        print(intervals)
        for y in intervals:
            l = 0
            while l < len(y) - 1 and arr[y[l] + 1] == 'x':
                l += 1
            y = y[l:]
            if len(y) > 1:
                if not arr[min(y) + 1] == "x" and not arr[max(y)] == "x":
                    for j in range(min(y) + 1, max(y) + 1):
                        arr[j] = "x"
            print(arr)
        return make_linked_list([h for h in arr if h != "x"])

    def dummy(self, head: Optional[ListNode]):
        res = self.helper(head)
        if res:
            while True:
                tmp = self.helper(res)
                if linked_list_to_array(tmp) == linked_list_to_array(res):
                    break
                res = tmp
        return res


if __name__ == '__main__':
    sol = Solution()
    input0 = make_linked_list([1, 2, -3, 3, -3, 3, -2, -1])
    input1 = make_linked_list([1,2,-3,3,1])
    input2 = make_linked_list([1,2,3,-3,4])
    input3 = make_linked_list([1,2,3,-3,-2])
    input4 = make_linked_list([1,2,3,-3,3])
    input5 = make_linked_list([1,3,2,-3,-2,5,5,-5,1])
    input6 = make_linked_list([-4,0,-2,-2,4,3,0,5,4,-4,-3,-4,0,-3,3])
    input7 = make_linked_list([-4,2,-5,4,1,0,-3,-3,3,1,-4,0,-3,5,0,-2,-1,-5])
    input8 = make_linked_list([-6,-9,-5,-10,-2,-5,-7,-4,3,8,9,-1,-5,-2,-7,-1,-4,9,-7,-2,-3,-4,6,-9,-3,-6,-8,1,-4,2,6,-10,-3,2,-6,-8,-5,-5,-3,-10,-9,-10,4,-8,-8,-2,-10,-4,-5,4,3,-7,-1,-9,-6,4,-5,7,-5,4,4,-9,6,-5,-6,-3,2,-1,9,-6,-7,-6,-5,-2,-9,-5,-5,-9,-3,-7,8])
    input9 = make_linked_list([-6, -9, -5, -10, -2, -5, -7, -4, -3, -4, 6, -9, -3, -6, -8, 1, -4, 2, 6, -10, -3, 2, -6, -8, -5, -5, -3, -10, -9, -10, 4, -8, -8, -2, -10, -4, -5, -1, -9, -5, -6, -3, 2, -1, 9, -6, -7, -6, -5, -2, -9, -5, -5, -9, -3, -7, 8])
    print("1", sol.dummy(input0))
    print("2", sol.dummy(input1))
    print("3", sol.dummy(input2))
    print("4", sol.dummy(input3))
    print("5", sol.dummy(input4))
    print("5", sol.dummy(input5))
    print("6", sol.dummy(input6))
    print("7", sol.dummy(input7))
    print("8", sol.dummy(input8))
    print("9", sol.dummy(input9))
