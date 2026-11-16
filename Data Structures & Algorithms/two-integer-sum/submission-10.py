class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums=sorted(nums)
        j=len(new_nums)-1
        i=0
        while new_nums[i]+new_nums[j]!=target:
            if new_nums[i]+new_nums[j]>target:
                j-=1
                continue
            if  new_nums[i]+new_nums[j]<target:
                i+=1
                continue
        if new_nums[i]==new_nums[j]:
            sol=[]
            sol.append(nums.index(new_nums[i]))
            sol.append(nums.index(new_nums[j], nums.index(new_nums[i])+1))
            return sorted(sol)
        sol=[]
        sol.append(nums.index(new_nums[i]))
        sol.append(nums.index(new_nums[j]))
        return sorted(sol)
