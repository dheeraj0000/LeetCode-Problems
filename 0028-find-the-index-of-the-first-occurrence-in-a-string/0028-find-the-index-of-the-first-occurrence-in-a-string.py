class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
	   # function  for creating lps table
        def lps(a):
            ans=[0]
            i=0
            j=1
            while j<len(a):
                if a[i]==a[j]:
                    i+=1
                    ans.append(i)
                    j+=1
                else:
                    if i==0:
                        ans.append(0)
                        j+=1
                    else:
                        i=ans[i-1]
            return ans
		# string matching using lps table
        i=0
        j=0
        if len(needle)==0:
            return 0
        h=lps(needle)

        while j<len(haystack):
       
            if i==len(needle)-1 and needle[i]==haystack[j]:
                return j-i
            if needle[i]==haystack[j]:
                i+=1
                j+=1
            else:
                if i==0:
                    i=0
                    j+=1
                else:
                    i=h[i-1]
                
        return -1
                
                        