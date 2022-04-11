import fileinput

ary = "[\"bulbasaur"
for line in fileinput.input(files='names.csv'):
    nLine = ", \""+line.strip()+"\""
    ary += nLine
print(ary+"]")

