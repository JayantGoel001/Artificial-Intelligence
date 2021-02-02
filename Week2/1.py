lines = []

with open("Sample Text.txt",'r+') as f:
    lines = f.read().split("\n")

print(lines)