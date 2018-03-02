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

    def __init__(self, File_Name, Calculations = None, File_Path_Read = "Medical-Software-Design/Assignments/HeartRateMonitor/test_data/"):
        self.File_Name = File_Name
        self.Data_Array = None
        self.Calculations = Calculations
        self.File_Path_Read = File_Path_Read



    def Read_File(self):
        """Read the CSV file into numpy array

	:param Data_Array: Convert CSV data into a numpy array
	:param File_Name: User specified file name

	"""
        logging.info("Reading the file into numpy array")
        filename = self.File_Path_Read + str(self.File_Name)
        Data = []
        
        try:
            Data = pd.read_csv(filename)
        except ImportError:
            logging.error("The user specified file could not be found")
            print("The specified file could not be found")

        self.Data_Array = np.array(Data) 

    def Write_File(self):
        """Take numpy array results and save as a JSON file.

        :param File_Name: User specified file name to save a JSON file

	"""

        File_Name_split = self.File_Name.split('.')
        File_Name_JSON = File_Name_split[0]

        logging.info("Writing JSON file called {}".format(File_Name_JSON))

        try:
            df = pd.DataFrame(np.array(self.Calculations))
        except TypeError:
            print("The Calculations did not result in expected data type. Check the original data file.")
	
        df.to_json(File_Name_JSON + '.json')   




