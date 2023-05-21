# Using ASCII format

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        m = {}
        ans = 0
        # Iterating through words
        for i in range(len(words)):
            val = words[i]
            morseCd = ""

            # Iterating through alphabets in words
            for j in range(len(words[i])):
                # ord() gives ASCII of letter words[i][j]
                # 97 is ASCII for 'a'
                # ord(words[i][j]) - 97 : index of letter words[i][j] in morse array
                morseCd = morseCd + morse[ord(words[i][j]) - 97]
            m[morseCd] = True
            
        ans = len(m.keys())
        return ans

# Creating Dict with alphabet:morseCd
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # Create morsedict with alphabet and correcponding morse code
        morsedict = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alpha)):
            morsedict[alpha[i]] = morse[i]
        
        print(morsedict)

        m = {}
        for i in range(len(words)):
            morseCd = ""
            for j in words[i]:
                morseCd = morseCd + morsedict[j]
            m[morseCd] = True
            print(m)
            
        ans = len(m.keys())

        return ans