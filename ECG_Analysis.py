
try:
    import numpy as np
except ImportError:
    print("Could not import numpy")

try:
    import sphinx
except ImportError:
    print("Could not import sphinx")

try:
    import logging
except ImportError:
    print("Could not import logging")


logging.basicConfig(filename="ECG_Project.txt", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%    M:%S %p')



class ECG():

    def __init__(self, Data_Array):
        logging.info("Initilizing class instance")

        self.Data_Array = Data_Array

        self.Mean_hr_bpm = None
        self.Voltage_Extremes = None
        self.Duration = None
        self.Num_Beats = None
        self.Beats = None
   

    def Method_Mean_hr_bpm():
        pass

    def Method_Voltage_Extremes():
        pass

    def Method_Duration(self):
        duration = self.Data_Array[-1,0]
        self.Duration = np.array([[duration]])

    def Method_Num_Beats():
        pass

    def Method_Beats():
        pass
   

  
