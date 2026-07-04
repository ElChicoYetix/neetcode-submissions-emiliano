class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset): # index, curr subset
            if i == len(nums): # llegar al final
                res.append(subset[::]) # [::] es una copy()
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            
            subset.pop()
            # All subsets that Do NOT inclde nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]: # while inbounds & same vals
                i += 1
            
            backtrack(i + 1, subset)

        backtrack(0, [])

        return res