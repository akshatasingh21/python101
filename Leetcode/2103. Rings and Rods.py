class Solution:
    def countPoints(self, rings: str) -> int:
        m = {}

        for i in range(0,len(rings),2):
            if rings[i+1] in m and rings[i] in m[rings[i+1]]:
                m[rings[i+1]][rings[i]] = m[rings[i+1]][rings[i]] + 1
            elif rings[i+1] in m:
                m[rings[i+1]][rings[i]] = 1
            else:
                m[rings[i+1]] = {}
                m[rings[i+1]][rings[i]] = 1

        cnt = 0
        for i in m.keys():
            if "R" in m[i] and "G" in m[i] and "B" in m[i]:
                cnt = cnt + 1
        
        print(m)
        return cnt
