# bme590hrm

This README explains how to use the ps178/bme590hrm project.

## ECG_Analysis.py
* This module includes a class that will take the filename of your ECG data file (can be CSV or JSON).
* The class will create attributes for the object based on the ECG data. These attributes include mean HR (bpm), min & max lead voltages, time duration of the ECG strip, number of detected beats in the ECG strip, and the number of times a beat has occured.

## test_ECG_Analysis.py
* This unit test will test each method used in ECG_Analysis module individually.

## Other
* requirements.txt file includes all the packages that are used for this project.

## Travis Badge:
[![Build Status](https://travis-ci.org/ps178/bme590hrm.svg?branch=master)](https://travis-ci.org/ps178/bme590hrm)
