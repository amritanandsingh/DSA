class Solution:
    def minCost(self, heights):
        if(len(heights) == 1):
            return heights[0]
        if(len(heights) == 2):
            return abs(heights[0] - heights[1])
        
            
        jumpFromLastStep = abs(heights[1] - heights[0])
        jumpFromSecondLastStep = 0
        ans= jumpFromLastStep
        
        i=2
        while i < len(heights):
            
            jumpFromLastStep = abs(heights[i-1] - heights[i]) 
            jumpFromSecondLastStep = abs(heights[i-2] - heights[i]) 
            
            ans =  min(jumpFromLastStep ,jumpFromSecondLastStep ) + ans
            i+=1
        return ans

obj = Solution()
heights = [20, 30, 40, 20]
print(obj.minCost(heights))
