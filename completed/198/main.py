class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        else:
            res = [nums[0], nums[1], nums[0] + nums[2]]
            for i in range(3, len(nums)):
                res.append(max(res[i-3], res[i-2]) + nums[i])
            return max(res)

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2,3,1]
    nums2 = [2,7,9,3,1]  # 12
    nums3 = [0]
    nums4 = [4,1,2,7,5,3,1]
    print(sol.rob(nums1))
    print(sol.rob(nums2))
    print(sol.rob(nums3))
    print(sol.rob(nums4))