from icecream import ic as print
from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        h = defaultdict(lambda: 0)
        res = ''
        for x in s:
            h[x] += 1
        for y in sorted(h.keys(), key=lambda z: h[z], reverse=True):
            res += h[y] * y
        return res

if __name__ == '__main__':
    sol = Solution()
    s1 = "tree"
    print(sol.frequencySort(s1))