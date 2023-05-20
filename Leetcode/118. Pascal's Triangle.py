class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row1 = [1]
        ans = [row1]
        for i in range(1,numRows):
            irow = [1]
            for j in range(i-1):
                irow.append(ans[i-1][j]+ans[i-1][j+1])
            irow.append(1)
            ans.append(irow)

        return ans