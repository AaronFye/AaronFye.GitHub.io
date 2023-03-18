import fileinput

bruh = 0

ary = "[\""
for line in fileinput.input(files='dict.txt'):
   if(len(line) == 5 ):
     nLine = ", \""+line.strip()+"\""
     ary += nLine 
     bruh = bruh + 1

   
print(ary+"]")
print(bruh)