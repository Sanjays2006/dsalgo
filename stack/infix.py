# def infix_to_postfix(s):
#     stack = []
#     output = []
#     precedence = {"+": 1,"-":1,"*":2,"/":2,"^":3}
#     for char in s:
#         if char.isalnum():
#             output.append(char)
#         elif char == "(":
#             stack.append(char)
#         elif char == ")":
#             while stack and stack[-1] != "(":
#                 output.append(stack.pop())
#             stack.pop()
#         else:
#             while stack and stack[-1] != "(" and precedence[char] <= precedence[stack[-1]]:
#                 output.append(stack.pop())
#             stack.append(char)

#     while stack:
#         output.append(stack.pop())
#     return "".join(output)
# str = "a+b*(c^d-e)^(f+g*h)-i"
# print(infix_to_postfix(str))




# Infix to prefix


def reverse(s):
    reverseStr = ""
    for char in s:
        if char == "(":
            reverseStr += ")"
        elif char == ")":
            reverseStr += "("
        else:
            reverseStr += char
    return reverseStr[::-1]

def infix_to_prefix(s):
    stack = []
    output = []
    precedence = {"+": 1,"-":1,"*":2,"/":2,"^":3}
    for char in s:
        if char.isalnum():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != "(" and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())
    result = "".join(output)
    return result[::-1]

str = "a+b*(c^d-e)^(f+g*h)-i"
expres = reverse(str)
print(infix_to_prefix(expres))