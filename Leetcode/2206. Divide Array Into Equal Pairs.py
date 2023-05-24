class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        m = {}

        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] = m[nums[i]] + 1
            else:
                m[nums[i]] = 1

        for i in m.keys():
            if m[i]%2 == 1:
                return False
        
        return True