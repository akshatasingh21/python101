# O(n) Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            if target-nums[i] in m:
                return [m[target-nums[i]], i]
            m[nums[i]] = i



# O(n^2) Solution 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = 1
        for i in range(len(nums)-1):
            if flag == 0:
                break

            x = nums[i]

            for j in range(i+1, len(nums)):
                z = nums[j]
                if x+z == target:
                    flag = 0
                    list = [i,j]
                    break
        return list
