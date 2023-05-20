class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        m = {}
        for i in range(len(arr)):
            if arr[i] in m:
                m[arr[i]] = m[arr[i]] + 1
            else:
                m[arr[i]] = 1
        
        nl = []
        for j in range(len(arr)):
            if m[arr[j]] == 1:
                nl.append(arr[j])
        
        x = len(nl)
        if k<=x:
            return nl[k-1]
        else:
            return ""

