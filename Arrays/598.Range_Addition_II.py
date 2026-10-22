class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        r=m
        c=n
        for x,y in ops:
            r=min(r,x)
            c=min(c,y)
        return r*c
