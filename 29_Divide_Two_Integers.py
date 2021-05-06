    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        
        if dividend > 0:
            dividend = -dividend
            if divisor > 0:
                divisor = -divisor
                flag = 1
            else:
                flag = 0
        else:
            if divisor > 0:
                divisor = -divisor
                flag = 0
            else:
                flag = 1
        value = divisor
        q = 1
        res = 0
        while value >= MIN_INT // 2 and value + value >= dividend:
            value += value
            q += q
        
        while dividend <= divisor:
            while dividend > value:
                value >>= 1
                q >>= 1
            res += q
            dividend -= value
            
        if flag == 0:
            return -res
        else:
            return res if res <= MAX_INT else MAX_INT
            
                    
