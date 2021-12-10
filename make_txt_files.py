import os;
from sys import argv;
import glob;

current_path = os.getcwd()
new_path = current_path + "\\" + argv[1]
os.chdir(new_path)


texts = {}
all_txt_files = glob.glob('*.txt')
for i in range(len(all_txt_files)):
    inputFile = open(all_txt_files[i],'r')
    new_file_path = current_path + "\\new_lectures\\" + all_txt_files[i]
    outputFile = open(new_file_path,'x')
    count = True
    for line in inputFile:
        if (count):
            outputFile.write(line)
        count = not count
    inputFile.close()
    outputFile.close()