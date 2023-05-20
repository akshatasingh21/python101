class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        m = {}
        cnt = 0

        for i in range(len(allowed)):
            m[allowed[i]] = True

        print(m)

        for i in range(len(words)):
            flag = 1
            for j in range(len(words[i])):
                if words[i][j] in m:
                    continue
                else:
                    flag = 0
                    break
            if flag > 0:       
                cnt = cnt + 1
        
        return cnt