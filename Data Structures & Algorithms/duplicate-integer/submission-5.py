class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        length=len(nums)
        for i in range(length):
            hashmap[nums[i]]=i
        if len(hashmap)!=length:
            return True
        return False

                  