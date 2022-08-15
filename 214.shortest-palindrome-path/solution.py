from typing import List


class Solution:
    def findKMP(self, s: str) -> List[int]:
        s = s + '#' + s[::-1]
        lookup = [0] * len(s)
        
        i = 0
        j = 1
        while j < len(s):
            if s[i] == s[j]:
                lookup[j] = i + 1
                i += 1
                j += 1
            elif i > 0:
                i = lookup[i-1]
            else:
                j += 1
                
        return lookup
            
    def shortestPalindrome(self, s: str) -> str:
        lookup = self.findKMP(s)
        longest_prefix_suffix = lookup[len(lookup) - 1]
        substring = s[longest_prefix_suffix:]
        return substring[::-1] + s
    
sol = Solution()
print(sol.shortestPalindrome("aacecaaa"))
print(sol.shortestPalindrome("abcd"))
print(sol.shortestPalindrome("abbacd"))
print(sol.shortestPalindrome("aabba"))