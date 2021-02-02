def checkC(character_frequency):
    if '{' in character_frequency and '}' in character_frequency and '#' in character_frequency and character_frequency['{'] == character_frequency['}']:
        return True
    else:
        return False

def checkPython(character_frequency):
    if ':' in character_frequency:
        return True
    else:
        return False


lines = []

with open("Sample Text.txt", 'r+') as f:
    lines = f.read().split("\n")

character_frequency = {}

for line in lines:
    for word in line.split():
        for character in word:
            if character in character_frequency:
                character_frequency[character] += 1
            else:
                character_frequency[character] = 1

print(character_frequency)

# We can tell whether it is c or text not python always.

if checkC(character_frequency):
    print("It is C programming language.")
elif checkPython(character_frequency):
    print("It is Python Language.")
else:
    print("It a text file.")
