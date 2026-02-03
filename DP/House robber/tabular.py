class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        dp=[0]*len(nums)
        i=1
        dp[0]=nums[0]
        while i < len(nums):
            take = nums[i]
            if i > 1:
                take += dp[i-2]
            nonTake = dp[i-1]
            dp[i]=max(take,nonTake)
            i+=1
        print(dp)
        return max(dp[-1],dp[-2])

        