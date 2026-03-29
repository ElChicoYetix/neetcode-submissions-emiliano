class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        output = []
        q = collections.deque() # index, value is nums[q[]]

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop() # pop smaller values from q

            q.append(r)

            if l > q[0]: # remove left val from window
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output