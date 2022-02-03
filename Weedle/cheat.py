import fileinput

ary = "[\"bulbasaur"
for line in fileinput.input(files='8name.txt'):
    nLine = ", \""+line.strip()+"\""
    ary += nLine
print(ary+"]")