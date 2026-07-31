class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_map(s):
            map = {}
            for i in range(len(s)):
                map[s[i]] = map.get(s[i], 0) + 1
            return map

        corelation = []
        res = []
        for s in strs:
            map = create_map(s)
            found = False
            for hash, indx in corelation:
                if hash == map:
                    found = True
                    res[indx].append(s)
                    break
            if not found:
                corelation.append([map, len(corelation)])
                res.append([s])

        return res
                