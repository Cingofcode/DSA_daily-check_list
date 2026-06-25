class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0
        n=len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1