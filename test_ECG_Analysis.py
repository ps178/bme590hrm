# Unit test for ECG data analysis

import pytest
import numpy as np 
import os.path

# Testing Parse_Class.py file
def test_Read_File():
    from Class_Parse import Parse_Files # Get the class
    trial = Parse_Files(File_Name = 'test_data1.csv', Calculations = None)
    trial.Read_File()
    assert trial.Data_Array[0,-1] == pytest.approx(-0.145)

def test_Write_File():
    from Class_Parse import Parse_Files
    t1 = Parse_Files(File_Name = 'test1.csv', Calculations = [[1,2,3,6,7],[4,5]])
    t1.Write_File()
    assert os.path.isfile('test1.json')


# Testing ECG_Analysis.py file
def test_Mean_hr_bpm():
    pass

def test_Voltage_Extremes():
    from ECG_Analysis import ECG
    Object = ECG(Data_Array = np.array([[1,2],[3,4],[5,6],[7,8],[77,88]]))
    Object.Method_Voltage_Extremes()
    assert Object.Voltage_Extremes == ((88),(2))
    assert isinstance(Object.Voltage_Extremes, tuple) == True


    
def test_Duration():
    from ECG_Analysis import ECG
    Object = ECG(Data_Array = np.array([[1,2],[3,4],[5,6],[7,8],[77,88]]))
    Object.Method_Duration()
    assert Object.Duration == 77   
  



def test_Num_Beats():
    pass

def test_Beats():
    pass


# Testing ECG_All.py file

def test_All_Duration():
    pass



