class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashing solution
        # initially we need to check the lengths of both the strings
        if len(s) != len(t):
            return False
        # we initial a dictionary to store the integer values
        hashMap = defaultdict(int)
        for i in s:
            hashMap[i] = hashMap[i] + 1

        for i in t:
            hashMap[i] = hashMap[i] - 1

        for i in hashMap.values():
            if i != 0:
                return False
        
        return True
        
        
        