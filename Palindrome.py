from collections import deque

def is_palindrome(s):
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("hello"))