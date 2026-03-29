class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        # conteo de t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # si ya cumplimos el conteo de ese char
            if c in countT and window[c] == countT[c]:
                have += 1

            # contraer ventana
            while have == need:
                # actualizar resultado
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # quitar desde la izquierda
                left_char = s[l]
                window[left_char] -= 1

                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""