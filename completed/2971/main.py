from icecream import ic as print

class Solution:
    def dummy(self, nums):
        tmp = sorted(nums)
        sums = [0]
        for x in tmp[:-1]:
            sums.append(x + sums[-1])
        for i in range(len(tmp)-1, 0, -1):
            if tmp[i] < sums[i]:
                return tmp[i] + sums[i]
        return -1

if __name__ == '__main__':
    sol = Solution()
    input1 = [5,5,5]
    input2 = [1,12,1,2,5,50,3]
    input3 = [5,5,50]
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
