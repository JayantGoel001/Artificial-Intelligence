killer(butch).
married(mia,marsellus).
dead(zed).
kills(marsellus,X):-
    gives_footmassage(mia,X).
loves(mia,X):-
    good_dancer(X).
perosn_eats_food(jules,Food):-
    nutritious(Food);
    tasty(Food).