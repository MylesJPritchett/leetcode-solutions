class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for k in range(0, len(nums)):
                if i == k:
                    break
                if nums[i] + nums[k] == target:
                    return [i, k]