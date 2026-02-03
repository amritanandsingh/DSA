from typing import List

class Solution:
    def fun(self,nums,index,dp):
        if index<0:
            return 0
        if dp[index] != -1:
            return dp[index]
        res2 = nums[index]+ self.fun(nums,index-2,dp )
        res= self.fun(nums,index-1,dp)
        dp[index]=max(res,res2)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        dp=[-1] * (len(nums)+2)
        ans= self.fun(nums,len(nums)-1,dp)
        return ans

# Driver code
arr = [2, 1, 4, 9]
obj = Solution()
print(obj.maximumNonAdjacentSum(arr))
