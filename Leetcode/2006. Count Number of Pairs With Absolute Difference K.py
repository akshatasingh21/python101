class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        m = {}

        for i in range(len(nums)):
            print(count)
            target1 = nums[i] - k
            if target1 in m:
                count = count + m[target1]
            target2 = k + nums[i]
            if target2 in m:
                count = count + m[target2]

            # Add value in map
            if nums[i] in m:
                m[nums[i]] =  m[nums[i]] + 1
            else:
                m[nums[i]] =  1
            print(m)

        return count