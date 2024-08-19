class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsSum = sum(nums) #sum of all elements
        numsSet = set(nums) 
        numsSetSum = sum(numsSet) #sum of unique elements
        difference = numsSum - numsSetSum #sum of dublicates
        result = numsSetSum - difference 

        return result