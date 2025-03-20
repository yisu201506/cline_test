def calculator(expression):
    # Split into numbers and operators
    tokens = []
    current = ''
    for char in expression:
        if char in '+-*/':
            tokens.append(int(current))
            tokens.append(char)
            current = ''
        else:
            current += char
    tokens.append(int(current))
    
    # First pass for * and /
    i = 1
    while i < len(tokens) - 1:
        if tokens[i] == '*':
            tokens[i-1] = tokens[i-1] * tokens[i+1]
            del tokens[i:i+2]
        elif tokens[i] == '/':
            tokens[i-1] = tokens[i-1] // tokens[i+1]
            del tokens[i:i+2]
        else:
            i += 2
    
    # Second pass for + and -
    result = tokens[0]
    i = 1
    while i < len(tokens) - 1:
        if tokens[i] == '+':
            result += tokens[i+1]
        elif tokens[i] == '-':
            result -= tokens[i+1]
        i += 2
    
    return result
