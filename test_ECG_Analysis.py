#Unit test for ECG data analysis

import pytest
import numpy as np 


def main():
    test_Read_File()
    test_Mean_hr_bpm()
    test_Voltage_Extremes()
    test_Duration()
    test_Num_Beats()
    test_Beats()

def test_Read_File():
    from ECG_Analysis import ECG # Get the class
    trial = ECG(File_Name = 'test_data1.csv') #Using one of the data files as a test
    Test = np.array(trial.Data_Array)
    #assert Test[0] == -0.145
    print(trial.Data_Array)


def test_Mean_hr_bpm():
    pass

def test_Voltage_Extremes():
    from ECG_Analysis import ECG
    

def test_Duration():
    pass

def test_Num_Beats():
    pass

def test_Beats():
    pass

if __name__ == "__main__":
    main()
