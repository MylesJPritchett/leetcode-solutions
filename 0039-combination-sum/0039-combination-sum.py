class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        builder = []
        output = []
        def dfs(i):
            if i >= len(candidates):
                return
            if sum(builder) == target:
                if builder not in output:
                    output.append(builder.copy())
                return
            elif sum(builder) > target:
                return

            builder.append(candidates[i])
            dfs(i)

            dfs(i + 1)


            builder.pop()
            dfs(i + 1)
        
        dfs(0)
        return output
