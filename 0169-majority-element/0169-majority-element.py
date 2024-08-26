class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for ele in nums:
            d[ele] = d.get(ele,0) + 1
            if d[ele] > len(nums) //2:
                return ele
        