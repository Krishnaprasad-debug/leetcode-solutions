class Solution:
    def countDaysTogether(self, aA: str, lA: str, aB: str, lB: str) -> int:
        aA=list(map(str,aA.split("-")))
        lA=list(map(str,lA.split("-")))
        aB=list(map(str,aB.split("-")))
        lB=list(map(str,lB.split("-")))
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dp=[0]*14
        for i in range(12):
            dp[i+2]=days[i]+dp[i+1]
        Astart=dp[int(aA[0])]+int(aA[1])
        Aend=dp[int(lA[0])]+int(lA[1])
        Bstart=dp[int(aB[0])]+int(aB[1])
        Bend=dp[int(lB[0])]+int(lB[1])
        arrive=max(Astart,Bstart)
        end=min(Aend,Bend)
        if(arrive<=end):
            return end-arrive+1
        else:
            return 0
