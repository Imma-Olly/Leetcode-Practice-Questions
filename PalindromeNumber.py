def isPalindrome(self, x: int) -> bool:
        rev_num = 0
        if x < 0:
            return False
        else:
            while x > 0:
                rem = x % 10
                rev_num = (rev_num * 10) + rem
                x = x // 10
    
        if rev_num == x:
            return True
        else:
            return False