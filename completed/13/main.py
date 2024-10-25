from icecream import ic as print

class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        prev = 0
        for i in range(len(s)):
            tmp = numbers.get(s[i])
            if prev and prev < tmp:
                res += tmp - (2 * prev)
            else:
                res += tmp
            prev = tmp
        return res

if __name__ == '__main__':
    sol = Solution()
    s1 = "MCMXCIV"
    print(sol.romanToInt(s1))
