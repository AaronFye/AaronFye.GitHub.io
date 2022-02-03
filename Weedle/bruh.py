import fileinput
length = 0
appear = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
longest = 0
# Using fileinput.input() method
for line in fileinput.input(files='names.txt'):
    size = len(line)
    length += size
    if(size > longest):
        longest = size
        print(line)
    appear[size]+=1
    #if(size == 8):
       # print(line)

avg = length/897
#print(avg)
#print(appear[longest])

i = 0
for items in appear:
    print("there are ", appear[i], " ",(i-1), " letter names")
    i = i+1
