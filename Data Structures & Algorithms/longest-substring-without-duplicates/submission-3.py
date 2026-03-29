class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxS = 0
        l = 0
        valores = set()

        for r in range(len(s)):
            while s[r] in valores:
                valores.remove(s[l])
                l += 1
            
            valores.add(s[r])
            maxS = max(maxS, r - l + 1)

        return maxS