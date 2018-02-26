try:
    import glob
except ImportError:
    print("Could not import glob")

try:
    import numpy as np
except ImportError:
    print("Could not import numpy")

try:
    import sphinx
except ImportError:
    print("Could not import sphinx")






class ECG():

    def __init__(self, File_Name):
        self.File_Name = File_Name
        self.Data_Array = None
        self.Mean_hr_bpm = None
        self.Voltage_Extremes = None
        self.Duration = None
        self.Num_Beats = None
        self.Beats = None

    def Read_File(self):
        Data = [] # Create an empty array
        with open('%s' % self.File_Name,'r') as My_File: #Open the file for reading purposes only and then close it
            Data = My_Files.readlines()
        Data_Array = np.array(Data)
        self.Data_Array = Data_Array

   

    def Method_Mean_hr_bpm():
        pass

    def Method_Voltage_Extremes():
        pass

    def Method_Duration():
        pass 

    def Method_Num_Beats():
        pass

    def Method_Beats():
        pass
   
    def Write_JSON():

  
