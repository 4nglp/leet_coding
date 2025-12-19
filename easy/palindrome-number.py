class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = []
        while x > 0:
            rev.append(x % 10)
            x //= 10
        arr = rev[::-1]
        for i in range(len(arr)):
            if arr[i] != rev[i]:
                return False
        return True
