class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        val = 0
        for i in range(len(arr)):
            val = arr[i]
            for j in range(i+1,len(arr),1):
                if (val == 2*arr[j] or arr[j] == 2*val):
                    print(val,arr[j])
                    return True
        return False