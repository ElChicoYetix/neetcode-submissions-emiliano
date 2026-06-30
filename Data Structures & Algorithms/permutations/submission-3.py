class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums: # for every number, add to all existing permutations
            new_perms = []

            for p in perms: # go through every existing permutation
                for i in range(len(p) + 1): # insert each element into this permutation
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms