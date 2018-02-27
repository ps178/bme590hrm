# This class is used to read file and write file 

try:
    import numpy as np
except ImportError:
    print("Could not import numpy")

try:
    import logging
except ImportError:
    print("Could not import logging")

try:
    import sphinx
except ImportError:
    print("Could not import sphinx")

try:
    import pandas as pd
except ImportError:
    print("Could not import pandas")

class Parse_Files:
    """This is Parse_Files class.

    This class will convert a file (CSV or JSON) into numpy array AND take numpy array and write a JSON file.

    """

    def __init__(self, File_Name):
        self.File_Name = File_Name
        self.File_Type = None
        self.Data_Array = None
    

    def Read_File(self):
        filename = "Medical-Software-Design/Assignments/HeartRateMonitor/test_data/" + str(self.File_Name)
        print(filename)
        print(filename.endswith('*.csv')) 
        #if filename.endswith('*.csv'):
            #logging.info("Input is a CSV file")
        Data = []
        Data = pd.read_csv(filename)
        self.Data_Array = np.array(Data)

        #else:
            #logging.warning("The specified file is not CSV!")
         #   self.Data_Array = None 

    def Write_File(self):
        pass    




