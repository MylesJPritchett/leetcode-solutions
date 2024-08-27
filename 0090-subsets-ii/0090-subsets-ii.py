class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        builder = []
        output = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                if builder not in output:
                    output.append(builder.copy())
                return
            builder.append(nums[i])
            dfs(i + 1)
    
            builder.pop()
            dfs(i + 1)
    
        dfs(0)
        return output
    