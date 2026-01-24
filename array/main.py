from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        greaterNum = nums[0]
        indexOfNum = 0
        foundFlag = False
        # searching index where greater Num have to push
        for i in range(len(nums)):
            if greaterNum > nums[i]:
                foundFlag= True
                break
            greaterNum = nums[i]
            indexOfNum = i
        if foundFlag == True and indexOfNum == 0:
            tempG= greaterNum
            f = False
            for i in nums:
                if i > greaterNum:
                    greaterNum = i
                    f= True
                    break
            if f == False:
                nums.reverse()
                return
        # if all element is in sorted
        if foundFlag == False  and indexOfNum != len(nums)-1:
            nums.reverse()
        else: 
            # place where i have to write main algo
            # find first element index where i have to push greaterNum
            indexOfJustSmallerNumber = 0
            while nums[indexOfJustSmallerNumber] > greaterNum :
                indexOfJustSmallerNumber+=1
            while indexOfJustSmallerNumber < len(nums) and  nums[indexOfJustSmallerNumber] == nums[indexOfJustSmallerNumber+1]:
                indexOfJustSmallerNumber+=1    

            i =  indexOfNum 
            while i > indexOfJustSmallerNumber:
                temp = nums[i-1]
                nums[i] = temp
                i=-1
            
            nums[indexOfJustSmallerNumber] =  greaterNum
    
        
        """
        Do not return anything, modify nums in-place instead.
        """
        

if __name__ == "__main__":
    # Try different inputs here
    nums = [1,2,3]
    print("Before:", nums)

    Solution().nextPermutation(nums)

    print("After: ", nums)
