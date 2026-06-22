class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            i=0
            j=len(s)-1
            count=0
            while(i<j):
                if(s[i]==s[j]):
                    i+=1
                    j-=1
                else:
                    count=1
                    break
            if(count==0):
                return s
        return ""