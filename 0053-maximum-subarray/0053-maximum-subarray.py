class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        temp=0
        for i in range(len(nums)):
            if temp<0:
                temp=0
            temp+=nums[i]
            if temp>max_sum:
                max_sum=temp
        return max_sum