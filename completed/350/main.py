from icecream import ic as print
from collections import defaultdict

class Solution:
    def dummy(self, nums1, nums2):
        ht1 = defaultdict(lambda: 0)
        ht2 = defaultdict(lambda: 0)
        for x in nums1:
            ht1[x] += 1
        for y in nums2:
            ht2[y] += 1
        res = []
        it = ht1 if len(ht1) <= len(ht2) else ht2
        for z in it:
            if ht1[z] and ht2[z]:
                tmp = [z] * min(ht1[z], ht2[z])
                res.extend(tmp)
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = [1,2,2,1], [2,2]
    input2 = [4,9,5], [9,4,9,8,4]
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
