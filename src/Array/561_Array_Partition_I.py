class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in range(0,len(nums),2):
            minus = min(nums[i],nums[i+1])
            result += minus

        return int(result)