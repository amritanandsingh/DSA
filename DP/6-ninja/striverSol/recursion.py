class Solution:
    def fun(self,matrix,lastIndex):
        if lastIndex == 0:
            maxi=-1
            for i in range(3):
                if(maxi != lastIndex):
                    maxi = max(maxi,matrix[0][i])
            return maxi
        
        maxi=-1
        for j in range(3):
            if(j != lastIndex):
                maxi = max(maxi, self.fun(matrix,j) + matrix[lastIndex][j])
        return maxi
    def ninjaTraining(self, matrix):
        return self.fun(matrix,len(matrix)-1)


obj=Solution()

print(obj.ninjaTraining([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))