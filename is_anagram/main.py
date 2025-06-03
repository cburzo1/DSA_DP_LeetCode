def is_anagram(str1, str2):

    anagram = False

    list1 = list(str1)
    list2 = list(str2)

    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                list2.pop(j)
                break

    if not list2:
        anagram = True

    return anagram

print(is_anagram("leet", "etle"))
'''first_unique_char("aabb")
first_unique_char("z")
first_unique_char("abcde")
first_unique_char("aAbBcCdD")
first_unique_char("")'''