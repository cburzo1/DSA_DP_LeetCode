def find_s_in_str(s, str):
    found = 0

    for i in range(0, len(str)):
        if s == str[i]:
            found = found + 1

    return found

def find_first_occurrence_of_unique_str(str):
    arr = []
    first_unique = -1

    for i in range(0, len(str)):
        arr.append(find_s_in_str(str[i],str))

    for i in range(0, len(arr)):
        if arr[i] == 1:
            first_unique = i
            break

    return first_unique

'''print(find_s_in_str("l","leetcode"))
print(find_s_in_str("e","leetcode"))
print(find_s_in_str("t","leetcode"))'''

print(find_first_occurrence_of_unique_str("leetcode"))
print(find_first_occurrence_of_unique_str("loveleetcode"))
print(find_first_occurrence_of_unique_str("aabb"))
print(find_first_occurrence_of_unique_str("z"))
print(find_first_occurrence_of_unique_str("abcde"))
print(find_first_occurrence_of_unique_str("aAbBcCdD"))
print(find_first_occurrence_of_unique_str(""))