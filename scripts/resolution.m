%%% README
% per lanciare questo script bisogna creare una cartella 'matrices' e
% metterci dentro le matrici da analizzare
%%%
clear

% Test Matrix
files =  dir('matrices/');

for i = 3 : size(files, 1)
    disp(['Loading' ' ' files(i).name])
    matFile = load([files(i).folder, '/', files(i).name]);
    disp('Setting matrix A')
    A = matFile.Problem.A;
    disp('Compute exact solution xe')
    xe = ones(size(A, 1), 1);
    disp('Compute b')
    b = A * xe;
    allvars = whos;
    init_memory = sum([allvars.bytes]);

    %% Solve the system
    disp('Solving system with Cholesky factorization...')
    tic
    L = chol(A);
    Y = linsolve(L, b);
    x_sol = linsolve(L, Y);
    toc
    disp('Done')
    
    %% Check
    allvars = whos;
    ending_memory = sum([allvars.bytes]);
    if (uint8(x_sol) == xe)
        disp([ "La matrice: ", files(i).name])
        disp("Ok la soluzione e' corretta");
        e = norm(x_sol - xe) / norm(xe);
        fprintf("L'errore e' %d", e);
        fprintf("La memoria usata (in Byte) e' %d", (ending_memory - init_memory));
    end
end