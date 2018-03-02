
try:
    import numpy as np
    import sphinx
    import logging
    import matplotlib
    import scipy
    import peakutils
    import pandas as pd
except ImportError:
    print("Could not import numpy, sphinx, logging, matplotlib, scipy, peakutils or pandas")


logging.basicConfig(filename="ECG_Project.txt", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%    M:%S %p')

class ECG():
    """This is an ECG class for processing ECG data.

       :param Data_Array: ECG data array in numpy array format
       :param User_Min: User defined minute interval for mean HR calculation
       The class outputs mean HR, number of beats, time for each beat, max & min voltage, and total duration of ECG data

    """

    def __init__(self, Data_Array, User_Min):
        logging.info("Initilizing ECG class instance")
        
        self.User_Min = User_Min
        self.Data_Array = Data_Array
        self.Time = np.multiply(self.Data_Array[:,0],60)
        self.Voltage = self.Data_Array[:,1]

        self.Mean_hr_bpm = None
        self.Voltage_Extremes = None
        self.Duration = None
        self.Num_Beats = None
        self.Beats = None
    
#    @property
#    def Data_Array(self):
#        return self.__Data_Array

#    @Data_Array.setter
#    def Data_Array(self, Data_Array):
#        self.__Data_Array = Data_Array
#        self.Method_Mean_hr_bpm()
#        self.Method_Voltage_Extremes()
#        self.Method_Duration()

#    @property
#    def User_Min(self):
#        return self.__User_Min

#    @User_Min.setter
#    def User_Min(self):
#        self.__User_Min = User_Min
#        self.Method_Mean_hr_bpm()

    def Method_Mean_hr_bpm(self):
        logging.info("Detecting heart beat")
        
        Mean_Voltage = np.mean(self.Voltage)
        Norm = np.subtract(self.Voltage, Mean_Voltage)
        Correlation = np.correlate(Norm, Norm, 'same')
        
        try:
            Max = np.amax(Correlation)
        except ValueError:
            print("Correlation failed. Check your ECG data.")

        Correlation_Norm = np.divide(Correlation, Max)
        
        try:
            index = peakutils.indexes(Correlation_Norm, thres=0.1, min_dist=100)
        except ValueError:
            print("Program was not able to detect any peaks")
        Time_Beat = np.take(self.Time, index)        
	
        Time_Interval = np.subtract(Time_Beat[-1], Time_Beat[0])
        Nm_Beats = np.size(index)

        self.Num_Beats = Nm_Beats 
        self.Beats = Time_Beat

        if self.User_Min is None:
                logging.warning("User did not specify an interval for mean HR calculation")
                self.Mean_hr_bpm = np.array([np.divide(Time_Interval, Nm_Beats)])
        else:
                self.User_Min = np.multiply(self.User_Min, 60)
                Time_Beat[np.where(Time_Beat<self.User_Min)]
                self.Mean_hr_bpm = np.divide(np.subtract(Time_Beat[-1],Time_Beat[0]), np.size(Time_Beat))


    def Method_Voltage_Extremes(self):

        logging.info("Calculating max and min voltage values")
        Min = np.amin(self.Voltage)
        Max = np.amax(self.Voltage)

        self.Voltage_Extremes = ((Max),(Min))

    def Method_Duration(self):
	
        logging.info("Calculating time duration of the ECG data")

        duration = self.Time[-1]
        self.Duration = np.array([[duration]])


   

  
