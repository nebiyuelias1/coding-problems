from typing import List


class Solution:
    def buildLSP(self, s: str) -> List[int]:
        lsp = [0] * len(s)
        
        i, j = 1, 0
        
        while i < len(s):
            if s[i] == s[j]:
                lsp[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lsp[j-1]
                
        
        return lsp

    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        i = 0
        j = 0
        
        lps = self.buildLSP(needle)
        
        while i < n and j < m:

            
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                
                if j == m:
                    break
        
            elif j > 0:
                j = lps[j-1]
            else:
                i += 1
                
        return i - j if j == m else -1

s = Solution()
s.strStr('hello', 'll')