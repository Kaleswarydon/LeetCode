from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List
from itertools import combinations


null = None


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(curr_index: int, curr_combi: list, curr_combi_sum: int):
            if curr_combi_sum == target:
                res.append(curr_combi.copy())
                return None
            if curr_combi_sum > target or curr_index == len(candidates):
                return None
            curr_val = candidates[curr_index]
            curr_combi.append(curr_val)
            helper(curr_index + 1, curr_combi, curr_combi_sum + curr_val)
            curr_combi.pop()
            while curr_index + 1 < len(candidates) and candidates[curr_index] == candidates[curr_index + 1]:
                curr_index += 1
            helper(curr_index + 1, curr_combi, curr_combi_sum)

        candidates.sort()
        res = []
        helper(0, [], 0)

        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [1], 1
    input2 = [10,1,2,7,6,1,5], 8
    print(sol.combinationSum2(*input1))
    print(sol.combinationSum2(*input2))
