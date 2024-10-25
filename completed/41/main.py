class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = len(nums) + 1
        for i in range(len(nums)):
            try:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1
            except:
                pass
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2,0] #3
    nums2 = [3,4,-1,1] #2
    nums3 = [7,8,9,11,12] #1
    nums4 = [2,1] #3
    nums5 = [1,2,6,3,5,4] #7
    nums6 = [1,1] #2
    print(sol.firstMissingPositive(nums1))
    print(sol.firstMissingPositive(nums2))
    print(sol.firstMissingPositive(nums3))
    print(sol.firstMissingPositive(nums4))
    print(sol.firstMissingPositive(nums5))
    print(sol.firstMissingPositive(nums6))