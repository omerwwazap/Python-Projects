#Question1
#Question answer by Checking Off -------------------------------
def anagramSolution1(s1, s2):
    if len(s1) != len(s2):
        return False

    checking_off = list(s2)

    for char in s1:
        for i, other_char in enumerate(checking_off):
            if char == other_char:
                checking_off[i] = None
                break
        else:
            return False

    return True
print('Answer to Question 1')
print(anagramSolution1('abcd','dcba')) #should be true
print('======================================')
#-------------------------------------------------------
#Question2
#Question answer by Sort and Compare -------------------------------
def is_anagram2(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

print('Answer to Question 2')
print(is_anagram2('anagram','nagaram'))   #should be true
print('======================================')
#-------------------------------------------------------
#Question3
#Question answer by Count and Compare -------------------------------
def anagramSolution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for char in s1:
        pos = ord(char) - ord('a')
        c1[pos] += 1

    for char in s2:
        pos = ord(char) - ord('a')
        c2[pos] += 1

    if c2!=c1:
        return False
    return True

print('Answer to Question 3')
print(anagramSolution3('apple','pleap')) #true
print('======================================')
#-------------------------------------------------------