class Solution:
    def findErrorNums(self, nums):
        complete_set = [i for i in range(1, len(nums) + 1)]
        missing = list(set(complete_set).difference(set(nums)))[0]
        double = sum(nums) - sum(set(nums))
        res = [double, missing]
        return res

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2,2,4]
    nums2 = [1,1]
    nums3 = [2,2]
    print(sol.findErrorNums(nums1))
    print(sol.findErrorNums(nums2))
    print(sol.findErrorNums(nums3))