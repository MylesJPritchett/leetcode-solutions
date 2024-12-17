class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        encountered = set()
        for num in nums:
            if num in encountered:
                return True
            else:
                encountered.add(num)
        return False