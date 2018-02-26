#Unit test for ECG data analysis

import pytest
import numpy as np 


def test_Read_File():
    from Parse_Class import Parse_Files # Get the class
    trial = Parse_Files(File_Name = 'test_data1.csv') #Using one of the data files as a test
    Test = np.array(trial.Data_Array)
    #assert Test[0] == -0.145
    print(trial.Data_Array)


def test_Mean_hr_bpm():
    pass

def test_Voltage_Extremes():
    pass
    

def test_Duration():
    pass

def test_Num_Beats():
    pass

def test_Beats():
    pass

def test_Write_File():
    pass


