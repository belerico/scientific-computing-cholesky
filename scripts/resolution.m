%%% README
% per lanciare questo script bisogna creare una cartella 'matrices' e
% metterci dentro le matrici da analizzare
%%%

function []=resolution(matrix)
  % addpath(genpath(pwd()));
  [x, xe, solv_time, mem] = resolve(matrix);
  if ispc
    os = 'windows';
  elseif isunix
    os = 'linux';
  end
  if (uint8(x) == xe)
      e = norm(x - xe) / norm(xe);
      result = sprintf(['Resolving %s\nError: %d\nElapsed time: ' num2str(solv_time) ' seconds\nOccupied memory: %.2f MB\n\n'], matrix, e, mem / (1024 ^ 2));
      fid = fopen(['results' filesep 'matlab_' os '_results.txt'], 'a');
      fprintf(fid, result);
      fclose(fid);
  end
end

function [x, xe, solv_time, mem]=resolve(matrix)
  % Compute memory before cholesky decomposition
  vars = whos;
  init_memory = sum([vars.bytes]); 
  % for i = 1:length(vars)
  %     init_memory = init_memory + vars(i).bytes;
  % end
  M = load(['matrices', filesep, matrix]);
  A = M.Problem.A;
  clear M; 
  xe = ones(size(A, 1), 1);
  b = A * xe;
  t1 = tic;
  x = A \ b;
  solv_time = toc(t1);
  % Compute memory after cholesky decomposition
  vars = whos;
  ending_memory = sum([vars.bytes]);
  % for i = 1:length(vars)
  %   ending_memory = ending_memory + vars(i).bytes;
  % end
  mem = ending_memory - init_memory;
end
