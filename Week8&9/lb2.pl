mystery(_,0,1).
mystery(X,1,X).
mystery(X,N,Y):-
    N>1,
    X1 is X*X,
    N1 is N-1,
    mystery(X1,N1,Y).

