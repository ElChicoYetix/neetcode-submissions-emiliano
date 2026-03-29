class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        izq = 0
        der = izq + 1
        while izq < len(numbers):
            if der >= len(numbers):
                izq += 1
                der = izq + 1
                continue
            suma = numbers[izq] + numbers[der]
            if suma == target:
                return [izq + 1, der + 1]
            elif suma > target:
                izq += 1
                der = izq + 1
            else:
                der += 1