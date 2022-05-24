class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            remainder = target-nums[i]
            if remainder in compliments:
                return [compliments[remainder],i]
            else:
                compliments[nums[i]] = i
