import re

class Solution:
    def isPalindrome(self,s):
        s=re.sub(r'[^a-z0-9]','',s.lower())
        return s==s[::-1]
    
s=Solution()

print(s.isPalindrome("A man, a plan, a canal: Panama"))