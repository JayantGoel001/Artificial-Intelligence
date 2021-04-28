h(Nationality, Pet, Cigarette, Drink, Color).

zebra_owner(Owner):-
    houses(Hs),
    member(h(Owner,zebra,_,_,_),Hs).

water_drinker(Drinker):-
    houses(Hs),
    member(h(Drinker,_,_,water,_),Hs).


houses(Hs):-
    length(Hs,5),
    member(h(english,_,_,_,red),Hs),
    member(h(spanish,dog,_,_,_),Hs),
    member(h(_,_,_,coffee,green),Hs),
    member(h(ukraine,_,_,tea,_),Hs),
    adjacent(h(_,_,_,_,green),h(_,_,_,_,white),Hs),
    member(h(_,serpent,winston,_,_),Hs),
    member(h(_,_,kool,_,yellow),Hs),
    Hs = [_,_,h(_,_,_,milk,_),_,_],
    Hs = [h(norwegian,_,_,_,_)|_],
    adjacent(h(_,fox,_,_,_),h(_,_,chesterfield,_,_),Hs),
    adjacent(h(_,_,kool,_,_),h(_,horse,_,_,_),Hs),
    member(h(_,_,lucky_strike,juice,_),Hs),
    member(h(japanese,_,kent,_,_),Hs),
    adjacent(h(nowegian,_,_,_,_),h(_,_,_,_,blue),Hs),
    member(h(_,_,_,water,_),Hs),
    member(h(_,zebra,_,_,_),Hs).


adjacent(A,B,Ls):-
    append(_,[A,B|_],Ls).
adjacent(A,B,Ls):-
    append(_,[B,A|_],Ls).
