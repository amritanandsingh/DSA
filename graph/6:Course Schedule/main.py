import collections
from collections import deque
from typing import List
class Solution:
    def dfs(self , courseList , index , visited , parent = -1):
        visited[index]=1
        for i in courseList[index]:
                if visited[i] == 0:
                    if False == self.dfs(courseList, i, visited, index):
                        return False
                elif visited[i] == 1 and i != parent:
                    return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if(len(prerequisites) == 1):
            return True
        courseList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            courseList[course].append(prereq)
        visited = [0]*numCourses
        for i in range(numCourses):
            if visited[i] == 0:
                if False == self.dfs(courseList , i , visited):
                    return False
        
        return True


sol = Solution()
print(sol.canFinish(5 , [[1,4],[2,4],[3,1],[3,2]]))
print(sol.canFinish(2 , [[1,0],[0,1]]))
         
            
            



