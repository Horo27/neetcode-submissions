class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2

        sum_ = set([0])

        for curr_num in nums:
            for curr_sum in list(sum_):
                if curr_sum + curr_num not in sum_:
                    sum_.add(curr_sum + curr_num)
        return target in sum_
        