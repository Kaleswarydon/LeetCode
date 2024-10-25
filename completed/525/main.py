from icecream import ic as print
from collections import defaultdict
import heapq

class Solution:
    def dummy(self, nums):
        running_sums = []
        running_sum = 0
        for i, x in enumerate(nums):
            if x:
                running_sum += 1
            else:
                running_sum -= 1
            running_sums.append(running_sum)
        hash_table = defaultdict(lambda: [])
        for j, y in enumerate(running_sums):
            hash_table[y].append(j)
        if hash_table[0]:
            max_sub_array_len = max(hash_table[0]) + 1
        else:
            max_sub_array_len = 0
        for k in hash_table.values():
            if k:
                sub_array_len = max(k) - min(k)
                if sub_array_len > max_sub_array_len:
                    max_sub_array_len = sub_array_len
        return max_sub_array_len

if __name__ == '__main__':
    sol = Solution()
    input1 = [0,1] #2
    input2 = [0,1,0] #2
    input3 = [0,1,0,1,1] #4
    input4 = [0,0,1,0,0,0,1,1] #6
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
