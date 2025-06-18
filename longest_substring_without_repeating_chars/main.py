def longest_substring_without_repeating_chars(s):
    max_length = 0

    for i in range(0, len(s)):
        seen = []

        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.append(s[j])

        if len(seen) > max_length:
            max_length = len(seen)

    return max_length
print(longest_substring_without_repeating_chars("abcabcbb"))
print(longest_substring_without_repeating_chars("bbbbbb"))
print(longest_substring_without_repeating_chars("pwwkew"))
