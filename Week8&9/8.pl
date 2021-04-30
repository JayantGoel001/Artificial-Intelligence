% NOTE:
% 	- To run the program, execute the following query:
% 				start; printResult.
% 				
% 	- To see the status of each move the agent makes,
% 	  uncomment the first line of the first occurrence of
% 	  the predicate start_searching.
% 	

:- dynamic([
  world_size/1,	
  position/2,
  wumpus/1,
  noPit/1,
  noWumpus/1,
  maybeVisitLater/2,
  goldPath/1
]).

%% The starting point for execution
start:-
  % make sure to clear any previous facts stored
  retractall(wumpus(_)),
  retractall(noPit(_)),
  retractall(noWumpus(_)),
  retractall(maybeVisitLater(_,_)),
  retractall(goldPath(_)),

  % initializations
  init_board,
  init_agent,
  init_wumpus,

  % agent starts searching from [1, 1] cell
  start_searching([1, 1], []),

  % if any paths stored as possible to visit later, do so
  maybeVisitLater(PausedCell, LeadingPath),
  retract(maybeVisitLater(PausedCell, _)),
  start_searching(PausedCell, LeadingPath).

%% INITIALIZING THE BOARD WITH PITS & GOLD
init_board:-
  retractall(world_size(_)),
  assert(world_size([5, 5])),

  retractall(position(_, _)),
  assert(position(gold, [2, 3])),

  % positions of pits
  assert(position(pit, [3, 1])),
  assert(position(pit, [5, 1])),
  assert(position(pit, [3, 3])),
  assert(position(pit, [4, 4])),
  assert(position(pit, [2, 5])),

  assert(noPit([1, 1])).

%% INITIALIZING THE AGENT IN THE BOARD
init_agent:-
  assert(position(agent, [1, 1])).

%% INITIALIZING THE WUMPUS IN THE BOARD
init_wumpus:-
  assert(position(wumpus, [1, 3])),
  assert(noWumpus([1, 1])).


%% DEFINING THE PERCEPTORS

% Helper predicate to check if cell position given is valid in the board.
valid_position([X, Y]):- X>0, Y>0, world_size([P, Q]), X@=<P, Y@=<Q.

% Generate adjacent positions of a given position.
adjacent([X, Y], Z):- Left is X-1, valid_position([Left, Y]), Z=[Left, Y].
adjacent([X, Y], Z):- Right is X+1, valid_position([Right, Y]), Z=[Right, Y].
adjacent([X, Y], Z):- Above is Y+1, valid_position([X, Above]), Z=[X, Above].
adjacent([X, Y], Z):- Below is Y-1, valid_position([X, Below]), Z=[X, Below].

% A position is smelly if a cell with Wumpus is adjacent to it. There has to be at least one wumpus first.
is_smelly([X, Y]):-
  position(wumpus, Z), \+ noWumpus(Z),
  adjacent([X, Y], Z).

% A position is breezy if a cell adjacent to it contains pit.
is_breezy([X, Y]):- adjacent([X, Y], Z), position(pit, Z).

% A position is glittery if the cell contains gold.
is_glittery([X, Y]):- position(gold, Z), Z==[X, Y].



%% TAKING THE ACTIONS

% Utility predicate checking if two different matches can be found to ascertain Wumpus' location.
moreThanOneWumpus:-
  wumpus(X), wumpus(Y), X\=Y.

% Confirming there are no more than one possible recordings of Wumpus based on smell perceived,
% then killing Wumpus from a cell that aligns in a straight line with the Wumpus' cell.
killWumpusIfPossible(AgentCell):-
  wumpus([Xw, Yw]), \+ moreThanOneWumpus, 	% ascertain Wumpus' cell
  AgentCell=[Xa, Ya],
  (Xw==Xa; Yw==Ya),			% check Agent is in a cell that's in a straight line as Wumpus' cell
  assert(noWumpus([Xw, Yw])),		% record that Wumpus is not in the board anymore as it is considered killed
  format('~nAgent confirmed Wumpus cell to be ~w and shot an arrow from cell ~w.~nThe WUMPUS has been killed!~n', [[Xw, Yw], AgentCell]),
  retractall(wumpus(_)).


%% Searching takes place as a series of checkings. If and when the first predicate fails,
%  or completes, the second predicate of the same name is tried.

% Check if the cell contains gold
start_searching(Cell, LeadingPath):-
  % printStatus(Cell, LeadingPath),		% remove comment to print status at each move
  is_glittery(Cell),
  append(LeadingPath, [Cell], CurrentPath),
  % record the gold path if it's not already done
  \+ goldPath(CurrentPath), assert(goldPath(CurrentPath)).

% Check if the agent can perceive breeze in the cell
start_searching(Cell, _):-
  is_breezy(Cell).
  % format('BREEZE detected!~n').

% Check if the agent cannot perceive breeze.
% This is important as it gives CERTAINTY that adjacent cells do not have pit.
start_searching(Cell, _):-
  \+ is_breezy(Cell),
  adjacent(Cell, X),
  \+ noPit(X), assert(noPit(X)).

% Check if the agent can perceive smell at this cell.
% If smelly, record that adjacent cells may have Wumpus.
start_searching(Cell, _):-
  is_smelly(Cell),
  adjacent(Cell, X),
  \+ noWumpus(X), assert(wumpus(X)).

% If the cell doesn't have smell, record that the adjacent cells certainly do NOT have Wumpus.
start_searching(Cell, _):-
  \+ is_smelly(Cell),
  adjacent(Cell, X),
  \+ noWumpus(X), assert(noWumpus(X)),
  wumpus(Y), X==Y, retract(wumpus(Y)).

% Otherwise, try to see and do if it is feasible to kill Wumpus from this cell,
% then find neighboring cells that are safe and visit recursively.
start_searching(CurrentCell, LeadingPath):-
  (killWumpusIfPossible(CurrentCell); format('')),	% Kill Wumpus if possible, else do nothing.

  append(LeadingPath, [CurrentCell], CurrentPath),

  \+ is_glittery(CurrentCell),	% We don't wanna explore further if we reach the gold.

  % get adjacent cells 
  adjacent(CurrentCell, X), \+ member(X, LeadingPath),

  % if the adjacent cells are not safe, marked as maybe Wumpus or maybe Pit,
  % put these to maybeVisitLater, so if inferred later to be safe, we will visit later.
  (( noWumpus(X), noPit(X)) -> write('');
    (\+ maybeVisitLater(CurrentCell, _) -> assert(maybeVisitLater(CurrentCell, LeadingPath)); write(''))
  ),

  % Of those that the agent knows to be safe (no Wumpus/pit), start searching from them.
  noWumpus(X), noPit(X),
  start_searching(X, CurrentPath).



%% OUTPUTTING THE STATUS & RESULTS

% The first result type is NO gold paths found and print result accordingly. 
printResult:-
  \+ goldPath(_), write("==> Actually, no possible paths found! :(").

% The second result type is gold paths found, print the paths.
printResult:-
  goldPath(_), !, format('The following paths to the Gold are found: ~n'),
  forall(goldPath(X), writeln(X)).

% Print the status of any given cell from during the search.
printStatus(Cell, LeadingPath):-
  format('~n--------------- STATUS ---------------~nCurrently in ~w~nLeading path: ~w~n', [Cell, LeadingPath]),
  write('WUMPUS: '),
  forall(wumpus(X), writeln(X)),nl,
  write('NO PIT: '),
  forall(noPit(Y), writeln(Y)),
  write('NO WUMPUS: '),
  forall(noWumpus(Z), writeln(Z)),
  write('MAYBE VISIT LATER: '),
  forall(maybeVisitLater(M, _), writeln(M)),
  format('~n-----------------------~n~n').
