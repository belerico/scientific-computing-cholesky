%%% README
% per lanciare questo script bisogna creare una cartella 'matrices' e
% metterci dentro le matrici da analizzare
%%%

clear

% Test Matrix
files =  dir('matrices/')

for i = 3 : size(files, 1)
    
    A = load([files(i).folder, '/', files(i).name])
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
        display([ "La matrice: ", files(i).name])
        display("Ok la soluzione � corretta");
        e = norm(x_sol - xe) / norm(xe);
        display(sprintf("L'errore � %d", e));
        display(sprintf("La memoria usata (in Byte) � %d", (ending_memory - init_memory)));


    end
end