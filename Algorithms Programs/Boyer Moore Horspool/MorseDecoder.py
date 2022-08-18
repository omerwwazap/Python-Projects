# Write a python code which will use this binary tree while decoding Morse alphabet.
# You are asked to implement this tree like a complete binary-heap tree array.
# Find left and right child of each node indexes in this tree with the formulas that we used in binary heap (i.e. left= 2j, right= 2j+1)
# For a given Morse code like(given as a string):
# .-- .. - .... .-.- -- -.-- .-.- -... . ... - .-.- .-- .. ... .... . ...
# This program will display the decoded morse-code string as:
# WITH MY BEST WISHES
# If the given Morse Code is wrong


def treeSearch(arr, string):
    road = string.split()
    result = ""
    for word in road:
        i = 1
        for char in word:
            if char == "-":
                i = (i * 2) + 1
            elif char == ".":
                i = i * 2
            else:
                result = "Error at " + str(i) + "th position of the array :("
                return result
        result += arr[i] + " "
    return result


arr = [
    "",
    "start",
    "E",
    "T",
    "I",
    "A",
    "N",
    "M",
    "S",
    "U",
    "R",
    "W",
    "D",
    "K",
    "G",
    "O",
    "H",
    "V",
    "F",
    "Ü",
    "L",
    "",
    "P",
    "J",
    "B",
    "X",
    "C",
    "Y",
    "Z",
    "Q",
    "Ç",
    "İ",
    "5",
    "4",
    "$",
    "3",
    "?",
    "-",
    ".",
    "2",
    ",",
    ":",
    "+",
    ";",
    "*",
    "%",
    "#",
    "1",
    "6",
    "=",
    "/",
    "Ş",
    "ğ",
    "ö",
    "&",
    "8",
    "7",
    "9",
    "0",
    "",
    "",
    "",
    "",
    "",
]

string = input("Please enter your morse code ")
print(treeSearch(arr, string))
