class Solution:
    def minSwap(self, nums1, nums2):
        n = len(nums1)
        dp = [-1] * n

        def solve(ind):
            if ind == n:
                return 0

            if ind > 0 and (nums1[ind-1] >= nums1[ind] or nums2[ind-1] >= nums2[ind]):
                nums1[ind], nums2[ind] = nums2[ind], nums1[ind]
                val = 1 + solve(ind + 1)
                nums1[ind], nums2[ind] = nums2[ind], nums1[ind]  # Swap back
                return val

            elif ind > 0 and (nums1[ind-1] >= nums2[ind] or nums2[ind-1] >= nums1[ind]):
                return solve(ind + 1)

            else:
                if dp[ind] != -1:
                    return dp[ind]

                tempAns1 = solve(ind + 1)

                nums1[ind], nums2[ind] = nums2[ind], nums1[ind]
                tempAns2 = 1 + solve(ind + 1)
                nums1[ind], nums2[ind] = nums2[ind], nums1[ind]  # Swap back

                dp[ind] = min(tempAns1, tempAns2)
                return dp[ind]

        return solve(0)
                