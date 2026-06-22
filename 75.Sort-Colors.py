class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c=[0,0,0]
        for num in nums:
            if num==0:
                c[0]+=1
            elif num==1:
                c[1]+=1
            else:
                c[2]+=1
        i=0
        j=0
        while(j<3):
            while(c[j]>0):
                nums[i]=j
                i+=1
                c[j]-=1
            j+=1    