class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_ = {}
        if len(s1) > len(s2):
            return False
        for c in s1:
            dict_[c] = dict_.get(c, 0) + 1
        
        aux = dict_.copy()
        l, r = 0,0

        while r < len(s2): 
            if s2[r] in aux:
                aux[s2[r]] -=1
                if aux[s2[r]] == 0:
                    aux.pop(s2[r])
                if not aux:
                    return True
                r+=1
            elif s2[r] in dict_:
                aux[s2[l]] = aux.get(s2[l], 0) + 1
                l += 1
            else:
                r+=1
                l=r
                aux = dict_.copy()
        return False
                

            




