from typing import List

class Solution:
    def rob1(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[-1])

        i = 1
        ans = 0
        prev = nums[0]
        prev2 = 0
        while i < len(nums):
            take = 0

            if i >= 1:
                take = nums[i] + prev2

            ans = max(prev, take)
            prev2 = prev
            prev = ans
            i += 1
        return ans

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[-1])


        tempList1 = []
        tempList2 = []
        for i in range(0,len(nums)):
            print(i)
            if i != 0:
                tempList1.append(nums[i])
            if i != (len(nums)-1):
                tempList2.append(nums[i])
        print(tempList1)
        print(tempList2)
        
        return max(self.rob1(tempList1), self.rob1(tempList2))
