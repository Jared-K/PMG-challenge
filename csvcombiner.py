"""
Write a command line program that takes several CSV files as arguments. 
Each CSV file (found in the fixtures directory of this repo) will have the same columns. 
Your script should output a new CSV file to stdout that contains the rows from each of the inputs along with an 
additional column that has the filename from which the row came (only the file's basename, not the entire path). 
Use filename as the header for the additional column.
"""
import pandas as pd
import sys
import os


def check_args(argv):
    """
    check_args checks if the input arguments are entered correctly and if the input csv file paths exist exist
    return: True if arguements are correct, False if arguemnts are wrong
    """
    if (len(argv) < 2):
        print(f'Error: No input csv files detected, run the code below')
        print(f'python csvcombiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv')
        return False
    
    if (len(argv) < 3):
        print(f'Only 1 input csv file was detected "{argv[1]}", please include atleast 2 input csv files')
        return False

    for file_path in argv[1:]:
            if not os.path.exists(file_path):
                print(f'Error: File path not found for {file_path}')
                return False
    return True

def combine_csv_files(argv):
    """
    combine_csv_files (2 or more input csv files): Outputs a new CSV file to stdout that contains the rows from each of the inputs along with an 
    additional column that has the filename from which the row came.
    combine_csv_files (1 or 0 input csv files): Outputs error statement
    """
    if check_args(argv):
        files = argv[1:]
        dataframes = []

        for file in files:
            temp_df = pd.read_csv(file)
            filename = file.replace('./fixtures/', ' ')
            temp_df['filename'] = filename
            dataframes.append(temp_df)

        df = pd.concat(dataframes)

        print(df.to_csv(index=False, line_terminator='\n'))

        #df.to_csv("complete.csv", index=False)
    return

def main():
    combine_csv_files(sys.argv)

if __name__ == '__main__':
    main()