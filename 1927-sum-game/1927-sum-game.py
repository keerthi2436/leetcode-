class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        
        left = num[:n // 2]
        right = num[n // 2:]
        
        left_sum = sum(int(x) for x in left if x != '?')
        right_sum = sum(int(x) for x in right if x != '?')
        
        left_q = left.count('?')
        right_q = right.count('?')
        
        if (left_q + right_q) % 2 == 1:
            return True
        
        return left_sum - right_sum != 9 * (right_q - left_q) // 2