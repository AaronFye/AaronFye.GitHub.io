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
    appear[size]+=1
    if(size == 8):
        print(line)

avg = length/807
#print(avg)
#print(longest)

i = 0
for items in appear:
    #print("there are ")
  #  print(appear[i])
  #  print(i)
  #  print(" letter names")
    i = i+1
