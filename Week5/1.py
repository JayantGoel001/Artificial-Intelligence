from random import randint


class Individual:
    def __init__(self, gnome, fitness):
        self.gnome = gnome
        self.fitness = fitness


def rand_num(start, end):
    r = end - start
    rnum = start + randint(0, r)
    return rnum


def repeat(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return True
    return False


def mutatedGene(gnome, V):
    while True:
        r = rand_num(1, V)
        r1 = rand_num(1, V)
        if r1 != r:
            temp = gnome[r]
            gnome[r] = gnome[r1]
            gnome[r1] = temp
            break
    return gnome


def create_gnome(V):
    gnome = "0"
    while True:
        if len(gnome) == V:
            gnome += gnome[0]
            break
        temp = rand_num(1, V)
        if not repeat(gnome, chr(temp + 48)):
            gnome += chr(temp + 48)
    return gnome


def call_fitness(gnome):
    pass


def cooldown(temp):
    return 90 * temp / 100


def lessthan(t1, t2):
    return t1.fitness < t2.fitness
