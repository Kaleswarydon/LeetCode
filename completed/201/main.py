from icecream import ic as print

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = ""
        left = format(left, '031b')
        right = format(right, '031b')
        for l, r in zip(left, right):
            if l == r:
                res += l
            else:
                break
        while len(res) != 31:
            res += "0"
        return int(res, 2)

if __name__ == '__main__':
    sol = Solution()
    data1 = [5, 7]
    data2 = [0, 0]
    data3 = [1, 2147483647]
    data4 = [0, 2]
    data5 = [1, 4]
    data6 = [2, 6]
    data7 = [6, 7]
    data8 = [4, 5]
    data9 = [8, 10]
    data10 = [4, 6]
    data11 = [3, 3]
    data12 = [10, 15]
    print(sol.rangeBitwiseAnd(*data1))
    print(sol.rangeBitwiseAnd(*data2))
    print(sol.rangeBitwiseAnd(*data3))
    print(sol.rangeBitwiseAnd(*data4))
    print(sol.rangeBitwiseAnd(*data5))
    print(sol.rangeBitwiseAnd(*data6))
    print(sol.rangeBitwiseAnd(*data7))
    print(sol.rangeBitwiseAnd(*data8))
    print(sol.rangeBitwiseAnd(*data9))
    print(sol.rangeBitwiseAnd(*data10))
    print(sol.rangeBitwiseAnd(*data11))
    print(sol.rangeBitwiseAnd(*data12))