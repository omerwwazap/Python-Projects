#Write a program that inputs a two dimensional list and a one dimensional list from the
#user. The program should display an appropriate message if the given one dimensional
#list exists in the given two dimensional list or not. The program should continue to enter
#one dimensional list until the user enters an empty list.
#Sample Run:
#Number of rows for two dimensional list please: 3
#Enter 3 rows as a list of ints please:
#1 2 3
#4 5 6
#7 8 9
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Another list of ints please:
#4 5 6
#This list exists in the two dimensional list
#Another list of ints please:
#1 3 5
#This list does not exists in the two dimensional list
#Another list of ints please:
rowsize = int(input('Number of rows for two dimensional list please:'))
masterlist=[]
m=rowsize
for i in range(rowsize):
    print('Enter ',m,'of',rowsize, 'ints please: ')
    row = [int(x) for x in input().split()]
    m=m-1
    for i in range(len(row)):
        row[i] = int(row[i])
    masterlist.append(row)
print(masterlist)

print('Enter one int please to see if they exists or not in the master list: ')
lookfor = [int(x) for x in input().split()]
while len(lookfor)!=0:
    print('Enter one int please to see if they exists or not in the master list: ')
    lookfor = [int(x) for x in input().split()]

if lookfor in masterlist :
    print('Yes',lookfor,' found in List : ',masterlist)
else:
    print('No',lookfor,' found in List : ',masterlist)
