class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res = []

        def backt(arr, sum_, k):
            if sum_ == target:
                res.append(arr[:])
                return
            
            for i in range(k + 1, len(candidates)):
                if sum_ + candidates[i] > target:
                    return
                if i > 0 and i != k + 1 and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backt(arr, sum_ + candidates[i], i)
                arr.pop()
        backt([], 0, -1)
        return res