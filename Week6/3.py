#                    A  B  C  D
constraint_graph = [[0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [1, 0, 0, 0],
                    [0, 0, 0, 1]]

domains = {
    'A': ['e'],
    'B': ['w', 's', 'm'],
    'C': ['f', 'b', 'p'],
    'D': ['a', 'i', 'ch']
}
# The values s, m, b, and a should be eliminated.
# "s" and "m" are crossed off due to being incompatible with "e" based on constraint (ii).
# "b" is eliminated due to constraint (i).,and
# "a" is eliminated because there is no value for (B) that is compatible with "a" (based on constraint (iii))

# A=e, B=w, C=f and D=i