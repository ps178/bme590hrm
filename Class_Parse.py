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

logging.basicConfig(filename="ECG_Project.txt", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# CLASS

class Parse_Files:
    """This is Parse_Files class.

    This class will convert a file .csv into numpy array AND take numpy array and write a JSON file.

    """

    def __init__(self, File_Name, Calculations):
        self.File_Name = File_Name
        self.File_Type = None
        self.Data_Array = None
        self.Calculations = Calculations

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
        File_Name_split = self.File_Name.split('.')
        File_Name_JSON = File_Name_split[0]

        logging.info("Writing JSON file called {}".format(File_Name_JSON))
        df = pd.DataFrame(self.Calculations,columns = ["mean_hr_bpm","voltage_extremes","duration","num_beats","beats"])
        df.to_json(File_Name_JSON + '.json')   




