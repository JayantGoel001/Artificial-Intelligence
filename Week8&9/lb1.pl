addN(X,0,X).
addN(X,N,Y):-
    X1 is X+1,
    N1 is N-1,
    addN(X1,N1,Y).

