class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = {}
        count_substring = {}
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
            count_substring[s2[i]] = 1 + count_substring.get(s2[i], 0)

        # checas
        if count == count_substring:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):
        # for i in range(3, 7-1)
        # mueves (eliminas y agregas) y luego checas

            #eliminar el L
            #if el conteo de la letra > 1, resta uno. else, remove
            left_char = s2[l] #s2[0]
            count_substring[left_char] = count_substring.get(left_char) - 1
            if count_substring[left_char] == 0:
                del count_substring[left_char]

            l += 1

            #if R + 1 en el conteo, +1. else, sumar uno
            right_char = s2[r] #s2[3]
            count_substring[right_char] = count_substring.get(right_char, 0) + 1
            
            if count == count_substring:
                return True
                
            
        return False