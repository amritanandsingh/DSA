from typing import List

class Solution:
    def frogJump(self, heights):
        energy=[0]
        minToReachSecond=abs(heights[1] - heights[0])
        energy.append(minToReachSecond)
        i=2
        while i < len(heights):
            jumpFromLastStep = abs(heights[i-1] - heights[i]) + energy[i-1]
            jumpFromSecondLastStep = abs(heights[i-2] - heights[i]) + energy[i-2]
            
            energy.append(  min(jumpFromLastStep ,jumpFromSecondLastStep ) )
            i+=1
        return energy[-1]

                   



sol = Solution()
print(sol.frogJump([3, 10, 3, 11, 3]))