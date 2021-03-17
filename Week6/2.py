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
hired = {
    'Anmol': ['C#']
}
for hired_key, hired_value in hired.items():
    for requirements in hired_value:
        project_requirements[requirements] -= 1

