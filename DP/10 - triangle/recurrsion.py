from typing import List

class Solution:
    def fun(self, triangle , m , n):
        if m==0 and n == 0:
            return triangle[0][0]
        if m < 0 or n < 0   :
            return float("inf")

        justAbove = float("inf")
        if len(triangle[m]) > n and len(triangle[m-1]) > n:
            justAbove = self.fun(triangle , m-1 , n) 
        justAboveOfLeft = self.fun(triangle , m-1 , n-1)

        return min(justAbove , justAboveOfLeft) + triangle[m][n]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = float('inf')
        for i in range(len(triangle)):
            t = self.fun(triangle,len(triangle) -1 , i)
            ans = min(ans , t)

        return ans

obj = Solution()
print(obj.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))