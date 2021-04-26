#! /usr/bin/python3
#Python Program
#April Murphy

import sys

#shift = sys.argv[0]

#for line in sys.stdin:
#    message = line
#    if '.' == line.rstrip():
#        break
shift = sys.stdin.readline()
#message = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."
message = input()
shift = int(shift[0])



message = message.upper()
new = ''
for i in message:
    if i.isalpha():
        if ord(i)+shift > 90:
            i = chr( ord(i) + shift - 26)
            new = new+i
        else:
            i = chr( ord(i) +  shift )
            new = new +i
message = new
for i in range(len(message)):
    if i%50 == 0 and i!=0:
        print ("\n"+message[i], end='')
    elif i%5 == 0 and i!=0:
        print("\t" + message[i], end='')
    else:
        print(message[i],end='')

print()



