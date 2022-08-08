class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        minimum = float('inf')
        for i in range(k):
            for j in range(len(num)):
                new_num = num.replace(num[j], '', 1)
                if not new_num:
                    minimum = 0
                elif int(new_num) < minimum:
                    minimum = int(new_num)
            num = str(minimum)
                    
        return  str(minimum) if minimum < float('inf') else '0'
    

sol = Solution()
sol.removeKdigits("10001", 4)