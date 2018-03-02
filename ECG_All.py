#The main function that will call all the others


try:
    import logging
except ImportError:
    print("Could not import logging")

try:
    import sphinx
except ImportError:
    print("Could not import sphinx")

try:
    import numpy as np
except ImportError:
    print("Could not import numpy")

logging.basicConfig(filename="ECG_Project.txt", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def main():
    """This module is for performing various calculations on ECG data.

    This module will call upon two different classes (Class_Parse, and ECG_Analysis) to obtain the ECG data and perform ECG calculations. 

    """
    File_Name_Input = input("What is the name of the file containing the ECG data?")
    User_Min = input("What is the time interval (in mins) for the mean HR? (Type None for the overall average)")
    
    logging.infor("User inputted required values")
    Data_Array = Get_File(File_Name_Input)
    Results = Perform_Analysis(Data_Array, User_Min)
    Save_Results(File_Name_Input, Results)


def Get_File(File_Name_Input):
    """Calls the Class_Parse file for the Parse_Files class. Converts csv file to a numpy array.

    :param File_Name: Reads a CSV file. File name given by the user
    
    """
    from Class_Parse import Parse_Files
    Object = Parse_Files(File_Name = File_Name_Input, Calculations = None)
    Object.Read_File()
    Data_Array = Object.Data_Array
    
    logging.info("ECG Data obtained")
    return Data_Array

def Perform_Analysis(Data_Array, User_Min):
    """Calls the ECG_Analysis class to perform calculations on the ECG data.
    
    :param Data_Array: ECG data array in numpy array format
    :param User_Min: The user specified time interval

    """
    if User_Min is int:
        User_Min = User_Min
    else:
        User_Min = None

    from ECG_Analysis import ECG
    Object = ECG(Data_Array = Data_Array, User_Min = User_Min)
    Object.Method_Duration()
    Object.Method_Voltage_Extremes()
    Object.Method_Mean_hr_bpm()

    logging.info("ECG calculations performed")
    return (Object.Mean_hr_bpm, Object.Duration, Object.Voltage_Extremes, Object.Num_Beats, Object.Beats)

def Save_Results(File_Name_Input, Results):
    """Calls the Class_Parse again to save the ECG_Anaysis results as a JSON file

    :param File_Name_Input: The user specified file name that will become the file name of the JSON file created.
    :param Results: Results of the ECG analysis

    """
    from Class_Parse import Parse_Files
    Object = Parse_Files(File_Name = File_Name_Input, Calculations = Results)
    Object.Write_File()
    logging.info("Program ended")

if __name__ == "__main__":
    main()

