class Solution:
    def missingNum(self, arr):
        n=len(arr)+1
        s=set(arr)
        
        for i in range(1,n+1):
             if i not in s:
                 return i
        
