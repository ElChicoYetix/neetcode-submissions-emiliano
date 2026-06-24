class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total): # si total == target, o total > target...
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return

            cur.append(nums[i]) # agregamos el actual a cur

            dfs(i, cur, total + nums[i])

            cur.pop() # eliminar el nums[i] del final

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res