class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        for char in s:
            if char in brackets.values():
                stack.append(char)
            if char in brackets.keys():
                if brackets[char] in stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            print(char)
            print(stack)
        return len(stack) == 0
