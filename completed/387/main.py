from icecream import ic as print

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hist = [0] * 26
        for x in s:
            hist[ord(x) - 97] += 1
        for i, x in enumerate(s):
            if hist[ord(x) - 97] == 1:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    s1 = "leetcode"
    s2 = "loveleetcode"
    s3 = "aabb"
    print(sol.firstUniqChar(s1))
    print(sol.firstUniqChar(s2))
    print(sol.firstUniqChar(s3))