class Solution:
    def convertToTitle(self, num: int) -> str:
        s = ''
        
        while num>0:
            num -= 1
            rightmost = chr((num%26) + ord('A'))
            num //= 26
            s+=rightmost
            
        return s[::-1]