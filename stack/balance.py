def balance(s):
    stack = []
    pairs = {"}":"{",")":"(","]":"["}
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
s = "([])"
if balance(s):
    print("True")
else:
    print("False")