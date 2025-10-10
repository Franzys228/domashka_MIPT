def is_palindrome(s):
    return len(s) <= 1 or (s[0] == s[-1] and is_palindrome(s[1:-1]))
