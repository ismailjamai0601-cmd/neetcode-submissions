class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1={}
        hash_2={}
        for i in s:
            hash_1[i]=hash_1.get(i,0)+1 
        for j in t:
            hash_2[j]=hash_2.get(j,0)+1
        
        if hash_1==hash_2:
            return True
        return False
