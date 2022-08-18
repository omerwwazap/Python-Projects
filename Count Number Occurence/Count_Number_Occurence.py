# input (file with text,pattern)
# output (count number occurrence of pattern)

f = open("TEXT.txt", "r")


def readfile(file):
    file = f.read()  # read file
    file = file.lower().split()  # write file to string array as lowercase
    return file


def bubble(unsortedList):  # modified version the ones we used in java course
    length = len(unsortedList) - 1
    unsorted = True
    while unsorted:
        unsorted = False
        for element in range(0, length):
            if unsortedList[element] > unsortedList[element + 1]:
                hold = unsortedList[element + 1]
                unsortedList[element + 1] = unsortedList[element]
                unsortedList[element] = hold
                unsorted = True
    return unsortedList


def search3(list, pattern):
    fullcount = list.count(
        pattern
    )  # builtin python function to count number of occurrences
    return fullcount


text = readfile(f)
sortedlist = bubble(text)  # new sorted list

print("Your sorted list is ", text)  # debugging list
my_pattern = input("Give me a string to search: ")

answer = search3(
    sortedlist, my_pattern.lower()
)  # input "a,A" --> answer should be 7 || input is lowercase just as the list
if answer > 0:
    print('"', my_pattern, '"', "is found", answer, "times")
else:
    print('"', my_pattern, '"', "is not found")
