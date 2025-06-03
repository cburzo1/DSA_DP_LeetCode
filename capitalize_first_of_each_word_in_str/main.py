def capitalize_first_of_each_word_in_str(str):

    print(str)

    str2 = ""

    s = []

    str2 = str.split()

    print(len(str2) - 1)

    for i in range(0, len(str2)):
         s.append(str2[i][0].upper() + str2[i][1:len(str2[i])])

    return str2

print(capitalize_first_of_each_word_in_str("hello world"))
print(capitalize_first_of_each_word_in_str("PYTHON is AwEsoMe"))