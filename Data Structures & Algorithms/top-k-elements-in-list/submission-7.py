class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for i in nums:
            if i not in counter:
                counter[i]=1
            else:
                counter[i]+=1
        
        bucket=[]
        for i in range(len(nums)+1):
            bucket.append([])
        
        for i in counter:
            bucket[counter[i]].append(i)

        l_out = []
        i = -1
        while len(l_out) != k:
            for num in bucket[i]:
                l_out.append(num)
                if len(l_out) == k:
                    return l_out
            i -= 1

        return l_out

