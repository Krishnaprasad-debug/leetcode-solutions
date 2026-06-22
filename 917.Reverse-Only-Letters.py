class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ch=list(s)
        i=0
        j=len(ch)-1
        while(i<j):
            if(ch[i].isalpha()==False):
                i+=1
            elif(ch[j].isalpha()==False):
                j-=1
            else:
                ch[i],ch[j]=ch[j],ch[i]
                i+=1
                j-=1
        return "".join(ch)