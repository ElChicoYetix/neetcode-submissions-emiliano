
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        izq = 0
        der = len(numbers) - 1
        while izq < der: #mientras el izq no sea la ultima posicion
            suma = numbers[izq] + numbers[der]

            if suma == target:
                return [izq + 1, der + 1]

            if suma > target:
                der -= 1
            
            if suma < target:
                izq += 1