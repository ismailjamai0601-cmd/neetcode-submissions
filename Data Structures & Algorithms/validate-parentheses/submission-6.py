class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2):
            return False

        stack=[]
        for i in s:
            if i==")" or i=="}" or i=="]":
                if not len(stack):
                    return False

            if i=="(" or i=="{" or i=="[":
                stack.append(i)

            if i==")":
                if stack[-1]=="(":
                    l=stack.pop()
                    continue
                else: 
                    return False

            if i=="]":
                if stack[-1]=="[":
                    l=stack.pop()
                    continue
                else:
                    return False
            
            if i=="}":
                if stack[-1]=="{":
                    l=stack.pop()
                    continue
                else:
                    return False
        
        if not len(stack):
            return True
        return False