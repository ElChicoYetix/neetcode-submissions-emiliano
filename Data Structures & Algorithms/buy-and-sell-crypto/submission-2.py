class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inicio = prices[0]
        mayor_count = 0

        for i in range(len(prices)):
            if prices[i] < inicio:
                inicio = prices[i]   # ✅ guardas precio
            
            mayor_count = max(mayor_count, prices[i] - inicio)

        return mayor_count