from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[str] = []
        for token in tokens:
            if token == "+":
                stack.append(str(int(stack.pop()) + int(stack.pop())))
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(str(int(b) - int(a)))
            elif token == "*":
                stack.append(str(int(stack.pop()) * int(stack.pop())))
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(str(int(int(b) / int(a))))
            else:
                stack.append(token)
        return int(stack[0])
