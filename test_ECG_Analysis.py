#Unit test for ECG data analysis

import pytest

def test_Read_File():
    from ECG_Analysis import ECG # Get the class
    trial = ECG_Data(test_data1.csv) #Using one of the data files as a test
    assert ECG_Data[0,-1] == -0.145


def test_Mean_hr_bpm():


def test_Voltage_Extremes():


def test_Duration():


def test_Num_Beats():


def test_Beats():


