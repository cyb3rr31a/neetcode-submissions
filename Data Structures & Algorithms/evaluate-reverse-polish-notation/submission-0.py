class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        if tokens:
            for token in tokens:
                if token not in operators:
                    stack.append(int(token))
                else:
                    if stack:
                        num2 = stack.pop()
                        num1 = stack.pop()

                        if token == '+':
                            stack.append(num1 + num2)
                        elif token == '-':
                            stack.append(num1 - num2)
                        elif token == '*':
                            stack.append(num1 * num2)
                        elif token == '/':
                            if num2 != 0:
                                stack.append(int(num1 / num2))
                            else:
                                raise ValueError("Cannot divide by zero")

        return stack.pop()