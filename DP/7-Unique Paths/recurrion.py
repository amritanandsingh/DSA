class Solution:
    def fun(self , m,n,i,j):
        if i == 0 and j== 0:
            return 1
        if i < 0 or j < 0:
            return 0
        left = self.fun(m,n,i,j-1)
        up =  self.fun(m,n,i-1,j)
        return left + up
        

    def uniquePaths(self, m: int, n: int) -> int:
        return self.fun(m,n,m-1,n-1)
        
        
