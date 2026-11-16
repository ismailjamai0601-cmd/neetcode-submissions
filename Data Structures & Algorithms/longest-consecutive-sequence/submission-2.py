class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        
        no_double=sorted(list(hashmap.keys()))

        if len(no_double)==0:
            return 0
        
        if len(no_double)==1:
            return 1
        
        best=0
        length=1

        for i in range(len(no_double)-1):
            temp=no_double[i]
            
            if no_double[i+1]==(temp+1):
                length+=1

            if i==len(no_double)-2:
                best=max(length,best)
                break

            elif no_double[i+1]!=(temp+1):
                best=max(best, length)
                length=1
        
        return best

