class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = [num[0]]
        
        pop_count = 0
        n = len(num)
        
        for i in range(1, n):
            if len(stk) > 0:
                top_of_stack_element = int(stk[-1])
                
                while pop_count < k and top_of_stack_element > int(num[i]) and len(stk) > 0:
                    stk.pop()
                    pop_count += 1
                    if len(stk) > 0:
                        top_of_stack_element = int(stk[-1])
                    
                    
                stk.append(num[i])
            
        while pop_count < k:
            stk.pop()
            pop_count += 1
        
        joined_str = ''.join(stk)
        if not joined_str:
            return '0'
        
        return str(int(joined_str))
    

sol = Solution()
print(sol.removeKdigits("1432219", 3))
print(sol.removeKdigits("10200", 1))
print(sol.removeKdigits("10", 2))