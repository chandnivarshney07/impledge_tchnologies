# impledge_tchnologies


#Approach

1-Reading Input: The program reads words from a file (e.g., Input_01.txt) and stores them in a list.
2-Word Dictionary: It uses a set to enable fast lookups for words during the compound word verification process.
3-Recursive Check: The is_compounded function determines if a word is a compound using recursion and memoization to avoid redundant calculations.
4-Processing: The program iterates through all words, identifies compound words, and keeps track of the longest and second-longest words.
5-Performance: Execution time is measured in milliseconds to evaluate the efficiency of processing.

#How to Run the Program

1-Clone the repository or copy the script to your local machine.
2-Ensure you have the input files (e.g., Input_01.txt, Input_02.txt) in the same directory as the script. Each file should contain one word per line.
3-Run the script using Python:
python longest_compound_word.py
4-The program will output:
The longest compound word.
The second-longest compound word.
Time taken to process the file.

