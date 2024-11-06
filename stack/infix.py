def infix(string):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    
    stack = []
    output = []
    
    for char in string:
        if char.isalnum():  # If the character is an operand (number or letter)
            output.append(char)
        
        elif char == "(":  # If the character is '(', push it to the stack
            stack.append(char)

        elif char == ")":  # If the character is ')', pop until '('
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":  # Pop the '('
                stack.pop()
            else:
                print("Error: Unmatched parentheses")
                return
        
        else:  # If the character is an operator
            while (stack and stack[-1] != "(" and 
                   precedence[char] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(char)
        
    # Pop all the operators from the stack
    while stack:
        top = stack.pop()
        if top == "(":
            print("Error: Unmatched parentheses")
            return
        output.append(top)
        
    res = "".join(output)
    return res

# Test with the provided expression
expression = "((x + y)/(z - w))"
print(infix(expression))  # Should print "xy+zw-/"





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