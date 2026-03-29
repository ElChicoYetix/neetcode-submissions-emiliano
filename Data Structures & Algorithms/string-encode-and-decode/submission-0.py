class Solution:

    def encode(self, strs: List[str]) -> str:
        string_final = ""
        for word in strs:
            string_final = string_final + str(len(word)) + "#" + word
        
        return string_final

    def decode(self, s: str) -> List[str]:
        lista = []
        counter = 0

        while counter < len(s):
            contador_htag = counter

            while s[contador_htag] != "#":
                contador_htag += 1
            
            length = int(s[counter:contador_htag]) # sacar el numero antes del #

            lista.append(s[contador_htag + 1: contador_htag + 1 + length])
            
            counter = contador_htag + 1 + length

        return lista