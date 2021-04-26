#! /usr/bin/python3
#April Murphy
import sys


#Input
shift = sys.stdin.readline()
message = input().upper()
shift = int(shift)
new = ''

#Calculate cipher
for i in message:
    if i.isalpha():
        if ord(i)+shift > 90:
            i = chr( ord(i) + shift - 26)
            new = new+i
        else:
            i = chr( ord(i) +  shift )
            new = new +i
message = new

#Output
for i in range(len(message)):
    if i%50 == 0 and i!=0:
        print ("\n"+message[i], end='')
    elif i%5 == 0 and i!=0:
        print("\t" + message[i], end='')
    else:
        print(message[i],end='')
print()



