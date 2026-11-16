class Solution:
    def decodeString(self, s: str) -> str:

        string=f"{s[0]}" if s[0].isdigit() else f"'{s[0]}'"
        mydict={"[":"*(",
                "]":")"}
        for x in range(1,len(s)):
            letter=s[x]
            l2=s[x-1]
            if letter in mydict:
                string+=f"{mydict[letter]}"
            elif letter.isalpha():
                if l2=="]":
                    string+=f"+'{letter}'"
                else:
                    string+=f"'{letter}'"
            elif letter.isdigit():
                
                if l2.isalpha() or l2=="]":
                    string+=f"+{letter}"
                else:
                    string+=f"{letter}"

    

        return eval(string)
            