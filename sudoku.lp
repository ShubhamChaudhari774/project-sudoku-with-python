
% Rows, columns, and numbers
row(1..9).
col(1..9).
num(1..9).

% Each cell gets exactly one number
1 { sudoku(R,C,N) : num(N) } 1 :- row(R), col(C).

% Keep the initial numbers
:- initial(R,C,N), not sudoku(R,C,N).

% No repeated numbers in a row
:- sudoku(R,C1,N), sudoku(R,C2,N), C1 != C2.

% No repeated numbers in a column
:- sudoku(R1,C,N), sudoku(R2,C,N), R1 != R2.

% No repeated numbers in a 3x3 block
:- sudoku(R1,C1,N), sudoku(R2,C2,N),
   (R1-1)/3 == (R2-1)/3,
   (C1-1)/3 == (C2-1)/3,
   (R1,C1) != (R2,C2).

#show sudoku/3.
