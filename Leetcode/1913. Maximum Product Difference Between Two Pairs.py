class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        arr = nums

        arr.sort()
        mul1 = arr[len(arr)-2] * arr[len(arr)-1]
        mul2 = arr[0] * arr[1]

        return mul1-mul2