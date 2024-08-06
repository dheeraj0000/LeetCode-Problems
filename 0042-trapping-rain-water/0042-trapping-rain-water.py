class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i - 1])
        
        rightMax = [0] * n
        rightMax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])
        
        trappedWater = 0
        for i in range(n):
            waterLevel = min(leftMax[i], rightMax[i])
            trappedWater += waterLevel - height[i]
        
        return trappedWater