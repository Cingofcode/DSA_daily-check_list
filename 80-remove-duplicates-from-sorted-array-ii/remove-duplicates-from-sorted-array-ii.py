class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <2 :
            return len(nums)

        writepos=2
        for i in range(2,len(nums)):
            if nums[i] != nums[writepos-2]:
                nums[writepos] = nums[i]
                writepos+=1
        return writepos