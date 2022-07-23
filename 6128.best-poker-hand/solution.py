from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        flush = True
        for i in range(1, 5):
            if suits[i] != suits[i-1]:
                flush = False
                break
            
        if flush:
            return 'Flush'
        
        m = {}
        for rank in ranks:
            if rank in m:
                m[rank] = m[rank] + 1
            else:
                m[rank] = 1
        
        three = False
        pair = False
        for v in m.values():
            if v >= 3:
                three = True
            
            if v >= 2:
                pair = True
                
        if three:
            return "Three of a Kind"
        
        if pair:
            return "Pair"
        
        return "High Card"
    
    
s = Solution()
print(s.bestHand([10,10,2,12,9], ["a","b","c","a","d"]))