class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [ [] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, val in count.items():
            freq[val].append(key)
        
        left = k
        curr = len(freq) - 1
        res = []
        while left:
            if freq[curr]:
                res.append(freq[curr].pop())
                left -= 1
            else:
                curr -= 1
        
        return res