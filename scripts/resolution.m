%%% README
% per lanciare questo script bisogna creare una cartella 'matrices' e
% metterci dentro le matrici da analizzare
%%%
clear

% Test Matrix
files =  dir('../matrices/');
pid = feature('getpid')
plt = computer
fid = fopen([plt, "_matlab_var.txt"], 'w')
for i = 3 : size(files, 1)
    M = load([files(i).folder, '/', files(i).name]);
    xe = [];
    x_sol = [];
    init_memory = getMemoryUsage(pid);   
    xe = ones(size(M.Problem.A, 1), 1);
    b = M.Problem.A * xe;

    %% Solve the system
    disp('Solving system with Cholesky factorization...')
    tic
    x_sol = M.Problem.A \ b;
    toc
    ending_memory = getMemoryUsage(pid);
    disp('Done')
    %% Check
    if (uint8(x_sol) == xe)
        disp([ "La matrice: ", files(i).name])
  
        disp("Ok la soluzione e' corretta");
        e = norm(x_sol - xe) / norm(xe);
        disp(fprintf("L'errore e' %d", e));
        disp(fprintf("La memoria usata (in Byte) e' %d", (ending_memory - init_memory)));
    end
end
