from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:#
    def dummy2(self, tickets, k): #brute force
        tickets = deque([(i,x) for x, i in enumerate(tickets)])
        cntr = 0
        for i in range(k):
            tmp = tickets.popleft()
            tmp = (tmp[0] - 1, tmp[1])
            if tmp[0]:
                tickets.append(tmp)
            cntr += 1
        while True:
            tmp = tickets.popleft()
            tmp = (tmp[0] - 1, tmp[1])
            cntr += 1
            if not tmp[0] and tmp[1] == k:
                break
            if tmp[0]:
                tickets.append(tmp)
        return cntr

    def dummy(self, tickets, k):
        tickets = deque(tickets)
        cntr = 0
        for i in range(k):
            tmp = tickets.popleft() - 1
            if tmp:
                tickets.append(tmp)
            cntr += 1
        kth = tickets[0]
        tickets = [x - tickets[0] for x in tickets]
        neg = [y if y < 0 else -1 for y in [x for x in tickets[1:] if x <= 0]]
        pos = (len(tickets) - 1) - len(neg)
        cntr += kth * len(tickets)
        cntr -= pos
        cntr += sum(neg)
        return cntr

if __name__ == '__main__':
    sol = Solution()
    input1 = [2,3,2], 2 #6
    input2 = [5,1,1,1], 0 #8
    input3 = [84,49,5,24,70,77,87,8], 3 #154
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
