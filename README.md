# bme590hrm

This README explains how to use the ps178/bme590hrm project.

## Class_Parse.py
* This moculde includes a class that will take a csv file (specified by the user) and convert the ECG data into a numpy array. 
* This class will also take the results from another class (ECG_Analysis) and save the results as a JSON file.

## ECG_Analysis.py
* This module includes a classes that will take the ECG data as a numpy array and perform calculations. 
* Attributes include mean HR (bpm), min & max lead voltages, time duration of the ECG strip, number of detected beats in the ECG strip, and the number of times a beat has occured.

## test_ECG_Analysis.py
* This unit test will test each method used in ECG_Analysis module individually.

## Other
* requirements.txt file includes all the packages that are used for this project.

## Travis Badge:
[![Build Status](https://travis-ci.org/ps178/bme590hrm.svg?branch=master)](https://travis-ci.org/ps178/bme590hrm)
