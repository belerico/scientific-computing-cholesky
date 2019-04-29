clear;
matrices = cellstr(['Flan_1565'; 'StocF-1465'; 'cfd2'; 'cfd1'; 'G3_circuit'; 'parabolic_fem'; 'apache2'; 'shallow_water1'; 'ex15']);
for i = 1:9
  clear -x i matrices;
  if(exist(['../matrices/',  matrices{i}, '.mat'], 'file'))
    % load data
    disp('---')
    disp(['Loading matrix ', matrices{i}, '...'])
    load(['../matrices/',  matrices{i}, '.mat']); % crea una struct Problem con varie info, tra cui A
    disp('Matrix loaded')

    % set up vars
    A = Problem.A; % crea solo un nuovo reference, non duplica i dati
    clear Problem; % elimina tutte le info tranne A, salvata con l'altra var
    xe = ones(rows(A), 1);
    b = A * xe;
    memory_start = sum([whos.bytes]);

    % solve system
    disp('Solving system...')
    tic
    x = A \ b;
    toc
    disp('System solved')

    % results
    memory_finish = sum([whos.bytes]);
    if(uint8(x) == xe)
      memory = memory_finish - memory_start;
      relative_error = norm(x - xe) / norm(xe);
      disp(sprintf('Relative error: %d', relative_error))
      disp(sprintf('Memory used: %d Bytes', memory))
    else
      disp('Wrong result')
    endif
  else
    disp(['Matrix ', matrices{i}, ' not found']);
  endif
endfor