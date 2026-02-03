class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        prev=nums[0]
        lPrev=-1
        ans=0
        i=0
        while i < len(nums):
            curr = nums[i]
            if i > 1:
                curr += lPrev
            nonTake = prev
            ans=max(curr,nonTake)
            lPrev=prev
            prev=ans
            i+=1
        
        return ans