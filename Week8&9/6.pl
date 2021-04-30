count([],_,0).
count([X,Y|Rest],[X,Y],N) :-
    count(Rest,[X,Y],N1),
    N is N1 + 1.

count([Z|Rest],[X,Y],N) :-
    Z \= X,
    count(Rest, [X,Y], N).

votesFor([Cairo, London, Beijing, Moscow, Mumbai, Nairobi, Jakarta]) :-
    permutation([Cairo, London, Beijing, Moscow, Mumbai, Nairobi, Jakarta],[4,2,2,1,1,0,0]),
    (Cairo < Beijing; Cairo > Beijing),
    (Moscow = 4; Moscow = 0),
    (Cairo > Jakarta),
    count([Cairo, London, Beijing, Moscow, Mumbai, Nairobi, Jakarta], [0,2], 2),
    (Jakarta is (London-1);
    Jakarta is (Beijing-1)).

