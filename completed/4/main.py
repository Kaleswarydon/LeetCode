import statistics
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l_f = int((len(nums1) + len(nums2) + 1) / 2)
        l_c = -((len(nums1) + len(nums2) + 1) // -2)
        l = [l_f, l_c]
        ll = len(set(l)) == 1
        old = None
        for i in range(l_c):
            try:
                n1 = nums1[0]
            except:
                n1 = float("inf")
            try:
                n2 = nums2[0]
            except:
                n2 = float("inf")
            if n1 <= n2:
                tmp = nums1.pop(0)
            else:
                tmp = nums2.pop(0)
            if i == l_c - 1:
                if ll:
                    return tmp
                else:
                    return (old + tmp) / 2
            else:
                old = tmp

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print("med", statistics.median(sorted(nums1 + nums2)))
    print("sol", sol.findMedianSortedArrays(nums1, nums2))
