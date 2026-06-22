class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        ch=list(s)
        while(i<j):
            if(ch[i] in "aeiouAEIOU"):
                count=0
                if(ch[j] in "aeiouAEIOU"):
                    count=1
                    ch[i],ch[j]=ch[j],ch[i]
                    i+=1
                    j-=1
                if(count==0):
                    j-=1
            else:
                i+=1
        s="".join(ch)
        return s      