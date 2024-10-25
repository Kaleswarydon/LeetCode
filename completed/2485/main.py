from icecream import ic as print
from collections import defaultdict
import heapq

class Solution:
    def dummy(self, n):
        total_sum = ((n * (n + 1)) / 2)
        for i in range(1, n + 1):
            current_piv = ((i * (i + 1)) / 2)
            target_piv = (total_sum + i) / 2
            if current_piv == target_piv:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    input1 = 1
    input2 = 4
    input3 = 8
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
