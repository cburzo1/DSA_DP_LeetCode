import re

def is_palindrome(str):
    palindrome = False

    s = re.sub(r'[^a-zA-Z0-9]', '', str).lower()

    if s == s[::-1]:
        palindrome = True

    print(str[10:0])

    return palindrome

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))