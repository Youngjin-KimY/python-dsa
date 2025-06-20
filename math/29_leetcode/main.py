

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31 -1
        MIN = -2**31
        


        if dividend == 0:
            return 0

        if divisor == -1 and dividend == MIN:
            return MAX

        negative_result = False
        if divisor < 0 and dividend < 0 or divisor > 0 and dividend > 0:
            pass
        else:
            negative_result = True
    
            

        divisor, dividend = abs(divisor), abs(dividend)

        if dividend == 1:
            if divisor == 1:
                return -1 if negative_result else 1
            else:
                return 0
        
        # if dividend < divisor:
        #     return 0

        check_binary = 1
        while True:
            if dividend < (divisor*check_binary):
                # divisor >>= 1
                check_binary >>= 1
                break
            # divisor <<= 1
            check_binary <<= 1
        
        diff = dividend - (divisor*check_binary)

        cnt = 0
        if diff > 0:
            while diff > 0:
                diff -= divisor
                cnt += 1
            
            cnt -= 1

        res = check_binary + cnt
        if negative_result:
            res = -(res)
        
        return res
        
        
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN = -2 ** 31
        MAX = 2**31 - 1

        if divisor == -1:
            return max(min(MAX, -dividend), MIN)
        if divisor == 1:
            return dividend
        if dividend == divisor:
            return 1
        if dividend == -divisor:
            return -1

        quotient = 0

        sign = -1 if ((dividend > 0) ^ (divisor > 0)) else 1

        dividend, divisor = abs(dividend), abs(divisor)
        while dividend > 0:
            # print("dividend", dividend)
            muls = 1
            cDivisor = divisor
            while cDivisor <= dividend:
                # print("cDivisor", cDivisor)
                cDivisor <<= 1
                muls <<= 1
            # print("muls", muls)
            quotient += muls >> 1
            dividend -= cDivisor >> 1
        
        return max(min(sign * quotient, MAX), MIN)