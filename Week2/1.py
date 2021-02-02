lines = []

with open("Sample Text.txt", 'r+') as f:
    lines = f.read().split("\n")

words = []

for line in lines:
    for word in line.split():
        words.append(word)

characters = []
for word in words:
    for character in word:
        characters.append(character)

print("Number of Lines :", len(lines))
print("Number of Words :", len(words))
print("Number of Characters :", len(characters))