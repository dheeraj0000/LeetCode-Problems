class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]*(rowIndex+1)
        i = rowIndex
        for j in range(1,i):
            pascal[j] = (pascal[j-1] *i) //j
            i = i-1
        return pascal