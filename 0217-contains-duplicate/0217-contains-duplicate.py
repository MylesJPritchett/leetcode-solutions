#integer array with more than 1 number that is a small to medium number, could be positive or negative

#if a value appears twice then true

#if all distinct then false




class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False