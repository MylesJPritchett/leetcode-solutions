class Solution:
    def trap(self, height: List[int]) -> int:
        
        #O(1) memory and O(n) time
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        trapped = 0
        
        while l < r:
            if maxL < maxR:
                l = l + 1
                maxL = max(maxL, height[l])
                trapped = trapped + (maxL - height[l])
            else:
                r = r - 1
                maxR = max(maxR, height[r])
                trapped = trapped + (maxR - height[r])
        
        return trapped