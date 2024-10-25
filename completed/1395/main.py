from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        occurrences_left_smaller = [0 for _ in range(len(rating))]
        occurrences_left_larger = [0 for _ in range(len(rating))]
        occurrences_right_smaller = [0 for _ in range(len(rating))]
        occurrences_right_larger = [0 for _ in range(len(rating))]
        for i in range(len(rating)):
            for j in range(0, i):
                if rating[j] < rating[i]:
                    occurrences_left_smaller[i] += 1
                if rating[len(rating) - j - 1] < rating[len(rating) - i - 1]:
                    occurrences_right_smaller[len(rating) - i - 1] += 1
                if rating[j] > rating[i]:
                    occurrences_left_larger[i] += 1
                if rating[len(rating) - j - 1] > rating[len(rating) - i - 1]:
                    occurrences_right_larger[len(rating) - i - 1] += 1
        res = 0
        for k in range(len(rating)):
            res += occurrences_left_smaller[k] * occurrences_right_larger[k]
            res += occurrences_left_larger[k] * occurrences_right_smaller[k]
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [2,5,3,4,1]  # 3
    input2 = [2,1,3]  # 0
    input3 = [1,2,3,4]  # 4
    print(sol.numTeams(input1))
    print(sol.numTeams(input2))
    print(sol.numTeams(input3))
