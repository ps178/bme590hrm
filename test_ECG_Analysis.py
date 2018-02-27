# Unit test for ECG data analysis

import pytest
import numpy as np 


# Testing Parse_Class.py file
def test_Read_File():
    from Class_Parse import Parse_Files # Get the class
    trial = Parse_Files(File_Name = 'test_data1.csv') #Using one of the data files as a test
    trial.Read_File()
    assert trial.Data_Array[0,-1] == pytest.approx(-0.145)

def test_Write_File():
    pass


# Testing ECG_Analysis.py file
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



