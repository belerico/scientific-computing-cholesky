import os
import sys
import platform
from os import path
from pandas import pandas
if __name__ == "__main__" and __package__ is None:
    __package__ = "scripts.utils.get_statistics"
from ..definitions import BASE_DIR

def get_statistics(results_path):
    final_report = pandas.DataFrame(columns=['Tool', 'OS', 'Matrix', 'Relative error', 'Elapsed time', 'Mem', 'Min mem', 'Max mem', 'Avg mem', 'Delta mem'])
    profiler_report_row = 0
    for root, subdirs, files in os.walk(results_path):
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
                    row = lines[i_row].split()
                    if i_row % 5 == 0:
                        final_report.loc[int(i_row / 5 + script_report_row * (len(lines) / 5)), list(['Tool', 'OS', 'Matrix'])] = [splitted_name[1], splitted_name[0], row[1].rstrip()]
                    elif i_row % 5 == 1:    
                        final_report.loc[int(i_row / 5 + script_report_row * (len(lines) / 5)), 'Relative error'] = row[2].rstrip()
                    elif i_row % 5 == 2:    
                        final_report.loc[int(i_row / 5 + script_report_row * (len(lines) / 5)), 'Elapsed time'] = row[2].rstrip()
                    elif i_row % 5 == 3:    
                        final_report.loc[int(i_row / 5 + script_report_row * (len(lines) / 5)), 'Mem'] = row[2].rstrip()
                    i_row += 1
                script_report_row += 1
            # We're in some RESULTS_DIR subfolders 
            else:
                report = pandas.read_csv(pathname, delim_whitespace=True, usecols=[2], skiprows=1, header=None)
                final_report.loc[profiler_report_row, list(['Min mem', 'Max mem', 'Avg mem', 'Delta mem'])] = [float(report.min()), float(report.max()), float(report.mean()), float(report.max() - report.min())]
                profiler_report_row += 1
    final_report.to_csv(path.join(BASE_DIR, 'final-report_' + str.lower(platform.system()) + '.csv'), sep=';')

if __name__ == '__main__':
    get_statistics(sys.argv[1])