class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)) ==0:
            return 0
        
        insertpos = 1
        for i in range(0,len(nums)):
            if nums[i] != nums[insertpos -1]:
                nums[insertpos] = nums[i]
                insertpos+=1
        return insertpos
