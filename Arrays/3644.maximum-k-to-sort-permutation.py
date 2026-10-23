class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = None
        for i,x in enumerate(nums):
            if(x!=i):
                if ans is None:
                    ans=x
                else:
                    ans&=x
        return ans if (ans is not None) else 0 
