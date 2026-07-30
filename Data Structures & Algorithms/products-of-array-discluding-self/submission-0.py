class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        new=[0]*n
        
        for i in range(n):
            pdt=1
            for j in range(n):
                if i==j:
                    continue
                
                pdt*=nums[j]
            new[i]=pdt
        return new


        