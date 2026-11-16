class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for i in nums:
            counter[i]=counter.get(i,0)+1
        
        bucket=[]
        for i in range(len(nums)+1):
            bucket.append([])

        for num in counter:
            bucket[counter[num]].append(num)
        
        sol=[]
        i=len(bucket)-1
        while len(sol)!=k:
            if not len(bucket[i]):
                i-=1
                continue
            sol.extend(bucket[i])
            i-=1

        return sol
        
            
