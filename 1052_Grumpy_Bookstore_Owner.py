class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if len(customers) <= X:
            return sum(customers)
        res = 0
        for i, c in enumerate(customers):
            if grumpy[i] == 0:
                res += customers[i]
                
        temp = res
        for i in range(X):
            if grumpy[i] == 1:
                temp += customers[i]
        if temp > res:
            res = temp
        
        i = 0
        j = X - 1
        
        while j < len(customers):
            if grumpy[i] == 1:
                temp -= customers[i]
            i += 1
            j += 1
            if j < len(customers):
                if grumpy[j] == 1:
                    temp += customers[j]
                    if temp > res:
                        res = temp
        return res
                
            
                    
        
        

