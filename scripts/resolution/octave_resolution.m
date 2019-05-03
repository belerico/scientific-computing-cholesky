clear;
matrices = cellstr(['Flan_1565'; 'StocF-1465'; 'cfd2'; 'cfd1'; 'G3_circuit'; 'parabolic_fem'; 'apache2'; 'shallow_water1'; 'ex15']);
if ispc
  os = 'windows';
elseif isunix
  os = 'linux';
end
fid = fopen(['..', filesep, 'results', filesep, 'octave_', os, '_results.txt'], 'a');
fprintf(fid, strcat('octave_', os, '_results'), 'a');
fclose(fid);
for i = 1:length(matrices)
  clear -x i matrices;
  matrix_name = matrices{i};
  if(exist(['..', filesep, 'matrices', filesep, matrix_name, '.mat'], 'file'))
    % load data
    t = ctime(time);
    disp('---')
    disp(['Loading matrix ', matrix_name, '...'])
    load(['..', filesep, 'matrices', filesep, matrix_name, '.mat']); % crea una struct Problem con varie info, tra cui A
    disp('Matrix loaded')

    % set up vars
    A = Problem.A; % crea solo un nuovo reference, non duplica i dati
    clear Problem; % elimina tutte le info tranne A, salvata con l'altra var
    xe = ones(rows(A), 1);
    b = A * xe;
    solv_time = 0.0;
    memory_start = sum([whos.bytes]);

    % solve system
    disp('Solving system...')
    tic;
    x = A \ b;
    solv_time = toc;
    disp('System solved')

    % results
    memory_finish = sum([whos.bytes]);
    if(uint8(x) == xe)
      memory = memory_finish - memory_start;
      relative_error = norm(x - xe) / norm(xe);
      disp(sprintf('Elapsed time: %d seconds', solv_time));
      disp(sprintf('Relative error: %d', relative_error))
      disp(sprintf('Memory used: %d Bytes', memory))
      %write to file
      fid = fopen(strcat('../results/octave_', os, '_results.txt'), 'a');
      fprintf(fid, '\n\nMatrix name: %s\n', matrix_name);
      fprintf(fid, 'Starting at: %s', t);
      fprintf(fid, 'Elapsed time: %d seconds\n', solv_time);
      fprintf(fid, 'Relative error: %d\n', relative_error);
      fprintf(fid, 'Memory used: %d Bytes', memory);
      fclose(fid);
    else
      disp('Wrong result')
    endif
  else
    disp(['Matrix ', matrix_name, ' not found']);
  endif
  pause(5);
endfor