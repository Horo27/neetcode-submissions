class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix = [1 for _ in range(len(nums))]
        # postfix = [1 for _ in range(len(nums))]

        # prefix[0] = nums[0]
        # postfix[0] = nums[-1]

        # for i in range(1, len(nums)):
        #     prefix[i] = prefix[i-1] * nums[i]
        # for i in range(len(nums) - 2, -1, -1):
        #     postfix[i] = postfix[i+1] * nums[i]
        # result = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         result.append(postfix[0])
        #     elif i == len(nums) - 1:
        #         result.append(prefix[i-1])
        #     else:
        #         result.append(prefix[i-1] * postfix[i+1])
        # return result

        prod = 1
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                prod = prod * num
        
        if zeros >= 2:
            return [0 for _ in range(len(nums))]
        result = []

        if zeros == 1:
            for num in nums:
                if num == 0:
                    result.append(int(prod))
                else:
                    result.append(0)
        
        else:
            for num in nums:
                result.append(int(prod/num))
        return result
        