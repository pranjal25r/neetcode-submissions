class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackethash = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in brackethash:
                if stack and stack[-1] == brackethash[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

