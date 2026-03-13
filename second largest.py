class Solution:
    def getSecondLargest(self, arr):
        arr=list(set(arr))
        arr.sort()
        
        if len(arr)<2:
            return -1
        else:
            return arr[-2]
        

