class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]
        return output