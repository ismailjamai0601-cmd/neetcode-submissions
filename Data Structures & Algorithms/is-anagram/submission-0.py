class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        dictt={}  

        for c in s:
            if c not in dicts:
                dicts[c]=1
            if c in dicts:
                dicts[c]+=1

        for c in t:
            if c not in dictt:
                dictt[c]=1
            if c in dictt:
                dictt[c]+=1

        if len(dictt)!=len(dicts):
            return False
        
        for i in dicts:
            if (i not in dictt) or (dicts[i]!=dictt[i]):
                return False
        
        return True
