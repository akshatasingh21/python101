class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        m = {}

        for i in range(len(nums)):
            if nums[i] in m:
                count = count + m[nums[i]]
                m[nums[i]] = m[nums[i]] + 1
            else:
                m[nums[i]] = 1
            
        return count