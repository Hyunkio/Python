def is_valid_parentheses(s):
    stack = []
    matching_brackets = {')' : '(', '}' : '{', ']' : '['}
    
    for char in s:
        if char in matching_brackets.values(): #열린 괄호일 때
            stack.append(char)
        elif char in matching_brackets.keys(): #닫힌 괄호일 때
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    return len(stack) == 0

print(is_valid_parentheses("()[]{}"))
print(is_valid_parentheses("(]"))