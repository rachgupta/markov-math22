import os;
from sys import argv;
import glob;

#expects one command-line argument
current_path = os.getcwd()
new_path = current_path + "\\" + argv[1]
os.chdir(new_path)

#helper function to clean transcript files when copied directly from Panopto and create new files ready for main.py
texts = {}
all_txt_files = glob.glob('*.txt')
for i in range(len(all_txt_files)):
    #creates new file in other folder with every other line of og file
    #because panopto has timestamps every other line
    inputFile = open(all_txt_files[i],'r')
    new_file_path = current_path + "\\new_lectures\\" + all_txt_files[i]
    outputFile = open(new_file_path,'x')
    count = True
    for line in inputFile:
        if (count):
            outputFile.write(line)
        count = not count
    #closes files
    inputFile.close()
    outputFile.close()