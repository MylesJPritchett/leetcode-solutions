class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        builder = []
        output = []
        def dfs(i):
            if i >= len(nums):
                output.append(builder.copy())
                return
            builder.append(nums[i])
            dfs(i + 1)
    
            builder.pop()
            dfs(i + 1)
    
        dfs(0)
        return output
    