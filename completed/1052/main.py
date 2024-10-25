from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def dummy(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        not_grumpy = [1 if x == 0 else 0 for x in grumpy]
        customers_grumpy = [x * y for x, y in zip(customers, not_grumpy)]
        customers_grumpy_sum = sum(customers_grumpy)
        window_grumpy = customers_grumpy[:minutes]
        window_not_grumpy = customers[:minutes]
        window_grumpy_sum = sum(window_grumpy)
        window_not_grumpy_sum = sum(window_not_grumpy)
        max_diff = window_not_grumpy_sum - window_grumpy_sum
        for i in range(minutes, len(customers)):
            window_grumpy_sum -= customers[i - minutes] * not_grumpy[i - minutes]
            window_grumpy_sum += customers[i] * not_grumpy[i]
            window_not_grumpy_sum -= customers[i - minutes]
            window_not_grumpy_sum += customers[i]
            current_diff = window_not_grumpy_sum - window_grumpy_sum
            if max_diff < current_diff:
                max_diff = current_diff
        return customers_grumpy_sum + max_diff



if __name__ == '__main__':
    sol = Solution()
    input1 = [1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3  # 16
    input2 = [1], [0], 1  # 1
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
