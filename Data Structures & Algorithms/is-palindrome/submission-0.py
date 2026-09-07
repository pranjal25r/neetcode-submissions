class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""

        for c in s:
            if c.isalnum():
                palin += c.lower()
        return palin == palin[::-1]