class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        keyNew = key.replace(" ", "")

        mydict = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"

        # Declare index j for alpha
        j = 0
        for i in range(len(keyNew)):
            if keyNew[i] in mydict:
                continue
            else:
                mydict[keyNew[i]] = alpha[j]
                # Increment only when a new charater is entered in mydict
                j = j + 1

        ans = ""
        for i in message:
            if i != " ":
                ans = ans + mydict[i]
            else:
                ans = ans + " "  # Add spaces as is

        return ans
