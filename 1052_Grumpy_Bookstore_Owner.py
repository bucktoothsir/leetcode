class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if len(customers) <= X:
            return sum(customers)
        satisfied = 0
        not_satisfied = 0
        for i in range(X):
            if grumpy[i] == 1:
                not_satisfied += customers[i]
            else:
                satisfied += customers[i]
        i = 0
        j = X - 1
        temp = not_satisfied
        while j < len(customers):
            if grumpy[i] == 1:
                temp -= customers[i]
            i += 1
            j += 1
                
            if j < len(customers):
                if grumpy[j] == 1:
                    temp += customers[j]
                    if temp > not_satisfied:
                        not_satisfied = temp
                else:
                    satisfied += customers[j]
        return  satisfied + not_satisfied
