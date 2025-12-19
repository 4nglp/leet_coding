class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        l = len(arr)
        while l > 0:
            if len(arr[l-1]) > 0:
                return len(arr[l-1])
            else:
                l-=1