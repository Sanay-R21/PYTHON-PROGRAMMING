class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        letters1 =  {}
        letters2 =  {}
        for i in range(len(s)):
            letters1[s[i]] = letters1.get(s[i],0)+1
            letters2[t[i]] = letters2.get(t[i],0)+1
        if letters1 ==  letters2:
            return True
        return False


    
        