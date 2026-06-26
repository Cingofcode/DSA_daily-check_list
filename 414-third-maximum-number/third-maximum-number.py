class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if num > first:
                # New largest: shift everything down
                third = second
                second = first
                first = num
            elif num > second:
                # New second largest: shift third down
                third = second
                second = num
            elif num > third:
                # New third largest
                third = num

    
        return third if third != float('-inf') else first