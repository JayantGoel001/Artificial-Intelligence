all_members([H],L2) :-
    member(H,L2).
all_members([H|T],L2) :-
    member(H,L2),
    all_members(T, L2).

or([H]) :-
    H,!.
or([H|_]) :-
    H,!.
or([_|T]) :-
    or(T).

solve(Carrie,Erma,Ora,Tracy) :-
    Carrie = [Carrie_scholarship, Carrie_major],
    Erma = [Erma_scholarship, Erma_major],
    Ora = [Ora_scholarship, Ora_major],
    Tracy = [Tracy_scholarship, Tracy_major],
    All = [Carrie,Erma,Ora,Tracy],
    all_members([25000, 30000, 35000, 40000], [Carrie_scholarship, Erma_scholarship, Ora_scholarship, Tracy_scholarship]),
    all_members([astronomy, english, philosophy, physics], [Carrie_major, Erma_major, Ora_major, Tracy_major]),
    member([C1_scholarship,astronomy], All),
    Ora_scholarship > C1_scholarship,
    or([Ora_major = english, Ora_major = philosophy]),
    Erma_scholarship - Carrie_scholarship =:= 10000,
    member([C5_scholarship, english], All),
    Tracy_scholarship > C5_scholarship.





