class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        ans = []
        for i in range(len(arr)):
            ans.append("")
        print(ans)

        for i in range(len(arr)):
            word = arr[i]
            print(word)
            idx = int(word[-1])
            print(idx)
            ans[idx - 1] = word[0:len(word)-1]

        return " ".join(ans)
    
# Solution 2
import functools

class Solution:
    # Sorting using custom Comparator function
    def comp(self, a: str, b: str) -> int:
        if a[-1] > b[-1]:
            return 1
        return -1

    def sortSentence(self, s: str) -> str:
        # split string at space
        arr = s.split(" ")
        print(arr)

        # sort using custom comparator
        arr.sort(key=functools.cmp_to_key(self.comp))
        print(arr)

        # Remove last character
        for i in range(len(arr)):
            arr[i] = arr[i][0:len(arr[i])-1]
        print(arr)

        return " ".join(arr)