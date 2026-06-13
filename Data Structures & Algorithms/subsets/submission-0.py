class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        resultado = []
        nums.sort()

        def backtrack(inicio, actual):
            # agregar el subset actual al resultado final
            resultado.append(list(actual))

            # iterar sobre nums para generar los posibles subsets
            for i in range(inicio, len(nums)):
                # 1. skip duplicados
                if i > inicio and nums[i] == nums[i - 1]:
                    continue

                # 2. incluir nums[i] en el subset actual y moverse al siguiente
                actual.append(nums[i])
                backtrack(i + 1, actual)

                # 3. excluir nums[i] del subset actual (backtrack)
                actual.pop()
        
        backtrack(0, [])

        return resultado