class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        dict_ = {}

        for c in t:
            dict_[c] = dict_.get(c, 0) + 1
        
        sol = dict_.copy()
        min_ = [0, len(s) + 2]
        seen = {}
        l, r = 0, 0

        for r in range(len(s)):
            if s[r] in sol:
                sol[s[r]] -= 1
                if sol[s[r]] == 0:
                    sol.pop(s[r])
            elif s[r] in dict_:
                seen[s[r]] = seen.get(s[r], 0) + 1
            if len(sol):
                r += 1  
            while not sol:
                if min_[1] - min_[0] > r - l:
                    min_ = [l, r]    
                if s[l] in dict_:
                    if s[l] in seen:
                        seen[s[l]] -= 1
                        if seen[s[l]] == 0:
                            seen.pop(s[l])
                    else:
                        sol[s[l]] = sol.get(s[l], 0) + 1
                l += 1

        return s[min_[0]:min_[1]+1] if min_[1] != len(s) + 2 else ""
                        


            