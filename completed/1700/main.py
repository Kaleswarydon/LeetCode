from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode

class Solution:
    def dummy(self, students, sandwiches):
        students = deque(students)
        sandwiches = sandwiches[::-1]
        cntr = 0
        while cntr != len(sandwiches):
            if sandwiches[-1] == students[0]:
                sandwiches.pop()
                students.popleft()
                cntr = 0
            else:
                students.append(students.popleft())
                cntr += 1
        return len(students)


if __name__ == '__main__':
    sol = Solution()
    input1 = [1,1,0,0], [0,1,0,1] #0
    input2 = [1,1,1,0,0,1], [1,0,0,0,1,1] #3
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
