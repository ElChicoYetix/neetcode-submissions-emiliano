
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        izq = 0
        der = izq + 1
        while izq < len(numbers): #mientras el izq no sea la ultima posicion
            if der >= len(numbers): #si termina, resetea y suma 1 al izq
                izq += 1
                der = izq + 1
            suma = numbers[izq] + numbers[der]
            if suma == target:
                return [izq + 1, der + 1]
            elif suma > target: #si suma es mayor a target, resetea y suma 1 al izq
                izq += 1
                der = izq + 1
            else:
                der += 1 #si no, sigue buscando con el der