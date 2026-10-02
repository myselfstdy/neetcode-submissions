class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j] '''
        seen = {}
        for i , n in enumerate(nums):
            need = target -n
            if need in seen:
                return [seen[need],i]
            seen[n] = i
        