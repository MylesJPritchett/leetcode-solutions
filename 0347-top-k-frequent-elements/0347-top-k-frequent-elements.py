class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {}

        for i in nums:
            if i in frequencies:
                frequencies[i] = frequencies[i] + 1
            else:
                frequencies[i] = 1

        frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:k])

        return frequencies.keys()

        

        
            