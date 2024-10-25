from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_len = 0
        tmp_nums = []
        for n in nums:
            curr = str(n)
            max_len = max(max_len, len(curr))
            tmp_nums.append(curr)
        h = []
        for i in range(len(tmp_nums)):
            tmp_num = tmp_nums[i]
            while len(tmp_num) < max_len * 2:
                tmp_num += tmp_nums[i]
            heapq.heappush(h, (tmp_num[:max_len*2], tmp_nums[i]))
        res = ""
        while h:
            p = heapq.heappop(h)
            res += p[1][::-1]
        res = res[::-1].lstrip('0')
        if not res:
            res = '0'
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [10,2]  # "210"
    input2 = [3,30,34,5,9]  # "9534330"
    input3 = [34323,3432]  # "343234323"
    input4= [0,0]  # "0"
    print(sol.largestNumber(input1))
    print(sol.largestNumber(input2))
    print(sol.largestNumber(input3))
    print(sol.largestNumber(input4))
