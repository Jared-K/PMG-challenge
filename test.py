import unittest
import sys
import pandas as pd
from csvcombiner import combine_csv_files
from io import StringIO

class TestCSVcombiner(unittest.TestCase):
    def test_non_existent_file(self):
        capturedOutput = StringIO()      
        sys.stdout = capturedOutput   
        combine_csv_files(['csvcombiner.py', './fixtures/accesres.csv', './fixtures/clothing.csv'])               
        self.assertTrue("Error: File path not found for" in capturedOutput.getvalue())

    def test_one_input_csv_file(self):
        capturedOutput = StringIO()      
        sys.stdout = capturedOutput   
        combine_csv_files(['csvcombiner.py', './fixtures/accessories.csv'])               
        self.assertTrue("Only 1 input csv file was detected" in capturedOutput.getvalue())
    
    def test_no_file_path(self):
        capturedOutput = StringIO()      
        sys.stdout = capturedOutput
        combine_csv_files(['csvcombiner.py'])
        self.assertIn('Error: No input csv files detected, run the code below', capturedOutput.getvalue())

    def test_filename_column(self):
        capturedOutput = StringIO()      
        sys.stdout = capturedOutput
        combine_csv_files(['csvcombiner.py', './fixtures/accessories.csv', './fixtures/clothing.csv', './fixtures/household_cleaners.csv'])
        test_output = open("./test_output.csv", 'w+')
        test_output.write(capturedOutput.getvalue())
        test_output.close()
        df = pd.read_csv("./test_output.csv")
        self.assertIn("filename", df.columns.values)

if __name__=='__main__':
	unittest.main()