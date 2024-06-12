from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = sum(nums)  # Calculate the sum of all elements

        left = 0
        res = []
        for i in range(n):
            right -= nums[i]  # Subtract the current element from the right sum
            res.append(abs(left - right))  # Calculate the absolute difference and add it to the result list
            left += nums[i]  # Add the current element to the left sum

        return res