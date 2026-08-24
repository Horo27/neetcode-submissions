class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backt(sol, nro, nrc):
            if len(sol) == n * 2:
                res.append(sol[:])
                return
            if nro > nrc:
                backt(sol + ")", nro, nrc + 1)
            if nro < n:
                backt(sol + "(", nro + 1, nrc)
        backt("", 0, 0)
        return res