class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        T, wind = {}, {}

        for c in t:
            T[c] = 1 + T.get(c,0)
        
        res, reslen = [-1,-1], float("infinity")
        have, need = 0, len(T)
        l=0

        for r in range(len(s)):
            wind[s[r]] = 1 + wind.get(s[r],0)

            if s[r] in T and wind[s[r]] == T[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                wind[s[l]] -= 1
                if s[l] in T and wind[s[l]] < T[s[l]]:
                    have -= 1
                l += 1
        
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""


        
        
        

