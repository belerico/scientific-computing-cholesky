do
  clear;
  % choose matrix
  matrix_file_names = ['Annulla operazione'; 'Flan_1565.mat'; 'StocF-1465.mat'; 'cfd2.mat'; 'cfd1.mat'; 'G3_circuit.mat'; 'parabolic_fem.mat'; 'apache2.mat'; 'shallow_water1.mat'; 'ex15.mat'];
  matrices = cellstr(matrix_file_names);
  choice = menu('Choose matrix (1-10)', matrices{1}, matrices{2}, matrices{3}, matrices{4}, matrices{5}, matrices{6}, matrices{7}, matrices{8}, matrices{9}, matrices{10});
  if(choice >= 2 && choice <= 10 && exist(['../matrices/',  matrices{choice}], 'file'))
    % load data
    disp(['File: ', matrices{choice}]);
    load(['../matrices/',  matrices{choice}]); % crea una struct Problem con varie info, tra cui A

    % set up vars
    A = Problem.A; % crea solo un nuovo reference, non duplica
    clear Problem; % elimina tutte le info tranne A, salvata con l'altra var
    xe = ones(rows(A), 1);
    b = A*xe;
    clear matrix_file_names matrices choice again;
    memory_start = sum([whos.bytes]);

    % solve system
    tic;
    x = linsolve(A, b);
    %R = chol(A);
    %y = linsolve(R', b);
    %x = linsolve(R, y);
    toc;

    % results
    memory_finish = sum([whos.bytes]);
    memory = memory_finish - memory_start;
    relative_error = norm(x - xe) / norm(xe);
    disp(sprintf('Relative error: %d', relative_error));
    disp(sprintf('Memory: %d Bytes', memory));
    whos;
  else
    disp('matrix not chosen');
  endif

  again = yes_or_no('try again? ');
until(!again)