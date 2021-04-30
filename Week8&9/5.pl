exists(A,list(A,_,_,_,_)).
exists(A,list(_,A,_,_,_)).
exists(A,list(_,_,A,_,_)).
exists(A,list(_,_,_,A,_)).
exists(A,list(_,_,_,_,A)).

first(A,list(A,_,_,_,_)).
middle(A,list(_,_,A,_,_)).

rightOf(R,L,list(L,R,_,_,_)).
rightOf(R,L,list(_,L,R,_,_)).
rightOf(R,L,list(_,_,L,R,_)).
rightOf(R,L,list(_,_,_,L,R)).

nextTo(A,B,list(A,B,_,_,_)).
nextTo(A,B,list(_,A,B,_,_)).
nextTo(A,B,list(_,_,A,B,_)).
nextTo(A,B,list(_,_,_,A,B)).

nextTo(A,B,list(B,A,_,_,_)).
nextTo(A,B,list(_,B,A,_,_)).
nextTo(A,B,list(_,_,B,A,_)).
nextTo(A,B,list(_,_,_,B,A)).

puzzle(Houses):-
    exists(house(red,englishman,_,_,_),Houses),
    exists(house(_,spaniard,dog,_,_),Houses),
    exists(house(green,_,_,coffee,_),Houses),
    exists(house(_,ukraine,_,tea,_),Houses),
    rightOf(house(green,_,_,_,_),house(ivory,_,_,_,_),Houses),
    exists(house(_,_,snails,_,old_gold),Houses),
    exists(house(yellow,_,_,_,kool),Houses),
    middle(house(_,_,_,milk,_),Houses),
    first(house(_,norwegian,_,_,_),Houses),
    nextTo(house(_,_,_,_,chesterfields),house(_,_,fox,_,_),Houses),
    nextTo(house(_,_,_,_,kool),house(_,_,horse,_,_),Houses),
    exists(house(_,_,_,orange_juice,lucky_strike),Houses),
    exists(house(_,japanese,_,_,parliament),Houses),
    nextTo(house(_,norwegian,_,_,_),house(blue,_,_,_,_),Houses).


