project_requirements = {
    'C#': 2,
    'Flash': 2,
    'Photoshop': 1,
    'Database': 1,
    'Systems': 1
}
candidates = {
    'Palak': ['C#', 'Flash'],
    'Jayant': ['Photoshop', 'Flash'],
    'Jaideep': ['Flash', 'Systems'],
    'Jaya': ['C#', 'Database'],
    'Madhav': ['Photoshop', 'Flash'],
    'Bhawna': ['Systems', 'C#'],
    'Chandni': ['Photoshop', 'Flash']
}
candidates_reversed = {}
for key, value in candidates.items():
    for lang in value:
        if lang not in candidates_reversed:
            candidates_reversed[lang] = []
        candidates_reversed[lang].append(key)

print(candidates_reversed)
def candidateHired(project_requirements, hired):
    for hired_key, hired_value in hired.items():
        for requirements in hired_value:
            project_requirements[requirements] -= 1
    return project_requirements


hired = {
    'Anmol': ['C#']
}
print("Hired Candidates:\n")
print(hired)

numberOfCandidateToHire = 3
# For Job based Variable, there are three jobs J1,J2 and J3 representing 3 openings.The domains of all three variables are initially all the people.
# Then We can pose constraints which results in :
print(candidateHired(project_requirements, hired))

# Now we will use MRV(Minimum Remaining Value) and Degree heuristic
d = {}
for key, value in candidates_reversed.items():
    d[key] = len(value)
keys = sorted(d, key=d.get)

sorted_dic = []
for w in keys:
    sorted_dic.append((w, candidates_reversed[w]))

for i in range(numberOfCandidateToHire):
    if i < len(sorted_dic):
        domain = sorted_dic[i][0]
        for can in sorted_dic[i][1]:
            if can not in hired:
                hired[can] = []
            hired[can].append(domain)
        if len(hired)>=3+1:
            break

print("Hired Candidates:\n")
print(hired)
project_requirements = candidateHired(project_requirements, hired)
print(project_requirements)
