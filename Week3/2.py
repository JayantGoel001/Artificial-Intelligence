string = input("Enter An Expression to evaluate:\n")

l = []

if string[0]=="(" and string[-1]==")":
    string = string[1:-1]

multiply = string.split("*")

for i in multiply:
    if i.count('(')==i.count(')')!=0:
        if i[0]=='(' and i[-1]==')':
            l.append(i[1:-1].split("+"))
    else:
        l.append(i)

output_string = ""
for i in l:
    pass
