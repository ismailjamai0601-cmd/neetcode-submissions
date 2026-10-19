class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cle={}
        for i in range (len(strs)):
            temp=''.join(sorted(strs[i]))
            if temp not in cle:
                cle[temp]=[strs[i]]
            else:
                cle[temp].append(strs[i])
        result=list(cle.values())
        return result
    

