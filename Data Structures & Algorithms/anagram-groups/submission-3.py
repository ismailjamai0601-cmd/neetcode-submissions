class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol={}
        for i in strs:
            temp="".join(sorted(i))
            if temp not in sol:
                sol[temp]=[i]
            else:
                sol[temp].append(i)
        list_sol=list(sol.values())
        return list_sol
