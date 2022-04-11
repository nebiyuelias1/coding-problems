from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        
        if n > m or n == 0:
            return ''
        
        freq_t = Counter(t)
        freq_s = {}
            
        needs = len(freq_t.keys())
        haves = 0
        left = 0
        smallest_length = float('infinity')
        res = -1, -1
        
        for i in range(m):
            c = s[i]
            
            if c not in freq_t:
                continue
            
            freq_s[c] = freq_s.get(c, 0) + 1
            if freq_t[c] == freq_s[c]:
                haves += 1
            
            while haves == needs:
                length = (i - left) + 1
                if length < smallest_length:
                    res = left, i
                    smallest_length = length
                
                c = s[left]
                freq_s[c] = freq_s.get(c, 0) - 1
                
                if c in freq_t and freq_s[c] < freq_t[c]:
                    haves -= 1
                    
                left += 1
                
        
        left, right = res
        return '' if smallest_length == float('infinity') else s[left: right+1]
                
            
sol = Solution()
print(sol.minWindow('cabwefgewcwaefgcf', 'cae'))