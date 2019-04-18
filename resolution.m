clear

% Test Matrix
A = [
    1, 0, 0, 0, 0;
    0, 5, 0, 0, 0,
    0, 0, 4, 0, 0;
    0, 0, 0, 2, 0;
    0, 0, 0, 0, 1
    ];
xe = ones(size(A, 1), 1);
b = A * xe;

allvars = whos;
init_memory = sum([allvars.bytes]);

%% Solve the system
tic
L = chol(A);
Y = linsolve(L, b);
x_sol = linsolve(L, Y);

toc

%% Check

allvars = whos;
ending_memory = sum([allvars.bytes]);

if (uint8(x_sol) == xe)
    display("Ok la soluzione è corretta");
    e = norm(x_sol - xe) / norm(xe);
    display(sprintf("L'errore è %d", e));
    display(sprintf("La memoria usata (in Byte) è %d", (ending_memory - init_memory)));
    

end