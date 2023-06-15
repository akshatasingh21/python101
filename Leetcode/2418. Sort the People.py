class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        m = {}
        htarr = []
        nmarr = []
        for i in range(len(heights)):
            m[heights[i]] = names[i]

        heights.sort(reverse = True)
        
        for i in range(len(heights)):
            nmarr.append(m[heights[i]])
        print(nmarr)

        return nmarr