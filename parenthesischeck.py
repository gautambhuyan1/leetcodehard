def inputParenthesis():
    """
    Input a string of parentheses and return it.
    """
    return input("Enter a string of parentheses: ")


def isValidParenthesis(s: str) -> bool:

    stack = [0 for _ in range(len(s))]

    stackPtr = -1

    for c in s:
        print("Current character:", c, stackPtr, stack)
        if c == '(' or c == '{' or c == '[':
            stack[stackPtr + 1] = c
            stackPtr = stackPtr + 1
        elif c == ')' or c == '}' or c == ']':
            if stackPtr == -1:
                return False

            if (c == ')' and stack[stackPtr] != '('): return False
            if (c == ']' and stack[stackPtr] != '['): return False
            if (c == '}' and stack[stackPtr] != '{'): return False
            stackPtr = stackPtr - 1
    return True if stackPtr == -1 else False


inputStr = inputParenthesis()
print("Is the string of parentheses valid?", isValidParenthesis(inputStr))
