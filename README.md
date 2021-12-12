# Predictive Text via Markov Chains
#### Created as Final Project for Math22A at Harvard
## How to Use Our Project
### Cleaning the Files
First, you'll need all your transcripts of lectures off of Panopto in a directory within the directory of this repo. We have included some sample ones from Dr. Dusty Grundmeier's Fall 2021 Math22a class. 
To clean these files run the following code snippet with DIR_NAME replaced by the directory name with all the .txt files of the raw lectures
```bash
python make_txt_files.py DIR_NAME
```
We have provided a folder of raw_lectures and cleaned them using this program. The clean lecture files are in a directory called new_lectures
### Running the Predictive Text
Now, we run the main.py file with four command line arguments. 
```bash
python main.py "CLEAN_DIR_NAME" NUM_SENTENCES LIST_OF_STARTING_WORDS MAX_WORDS
```
For example, using our provided files, this will produce 3 sentences starting with I, You, and So with a max of 50 words per sentence. 
```bash
python main.py "new_lectures" 3 [i,you,so] 50   
```
