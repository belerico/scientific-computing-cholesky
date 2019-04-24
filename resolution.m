%%% README
% per lanciare questo script bisogna creare una cartella 'matrixes' e
% metterci dentro le matrici da analizzare
%%%

clear

% Test Matrix
files =  dir('matrixes/')

for i = 3 : size(files, 1)
    
    A = load([f(i).folder, '/', f(i).name])
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
end