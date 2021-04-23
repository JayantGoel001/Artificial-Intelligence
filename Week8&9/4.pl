wizard(ron).
wizard(X):-
    hasBroom(X),
    hasWand(X).

quidditchPlayer(harry).

hasBroom(X):-
    quidditchPlayer(X).

hasWand(harry).


