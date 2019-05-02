import os
from os import path
from pandas import pandas

CWD = path.dirname(path.abspath(__file__))
BASE_DIR = path.normpath(path.join(CWD, '..', '.'))
RESULTS_DIR = path.join(BASE_DIR, 'results')

if __name__ == '__main__':
    final_report = pandas.DataFrame(columns=['Tool', 'OS', 'Matrix', 'Relative error', 'Elapsed time', 'Mem', 'Min mem', 'Max mem', 'Avg mem'])
    profiler_report_row = 0
    for root, subdirs, files in os.walk(RESULTS_DIR):
        subdirs.sort()
        script_report_row = 0
        for f in sorted(files, key=str.lower):
            pathname = path.join(root, f)
            # We're in RESULTS_DIR root
            if files != [] and subdirs != []:
                # print(pathname)
                with open(pathname) as result:
                    lines = result.readlines()
                splitted_name = path.basename(pathname).split('_')
                # print(splitted_name)
                i_row = 0
                while i_row < len(lines):
                    row = lines[i_row].split(' ')
                    if i_row % 5 == 0:
                        final_report.loc[int(i_row / 5 + script_report_row * (len(lines) / 5)), list(['Tool', 'OS', 'Matrix'])] = [splitted_name[1], splitted_name[0], row[1].rstrip()]
                    elif i_row % 5 == 1:    
                        final_report.loc[int(i_row / 5 + script_report_row * (len(lines) / 5)), 'Relative error'] = row[1].rstrip()
                    elif i_row % 5 == 2:    
                        final_report.loc[int(i_row / 5 + script_report_row * (len(lines) / 5)), 'Elapsed time'] = row[2].rstrip()
                    elif i_row % 5 == 3:    
                        final_report.loc[int(i_row / 5 + script_report_row * (len(lines) / 5)), 'Mem'] = row[2].rstrip()
                    i_row += 1
                script_report_row += 1
            # We're in some RESULTS_DIR subfolders 
            else:
                report = pandas.read_csv(pathname, sep=' ', usecols=[1], skiprows=1, header=None)
                final_report.loc[profiler_report_row, list(['Min mem', 'Max mem', 'Avg mem'])] = [float(report.min()), float(report.max()), float(report.mean())]
                profiler_report_row += 1
    print(final_report.head(n = 15))