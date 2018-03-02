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

def main():
    File_Name_Input = input("What is the name of the file containing the ECG data?")
    User_Min = input("What is the time interval (in mins) for the mean HR? (Type None for the overall average)")

    Data_Array = Get_File(File_Name_Input)
    Results = Perform_Analysis(Data_Array, User_Min)
    Save_Results(File_Name_Input, Results)


def Get_File(File_Name_Input):
    from Class_Parse import Parse_Files
    Object = Parse_Files(File_Name = File_Name_Input, Calculations = None)
    Object.Read_File()
    Data_Array = Object.Data_Array

    return Data_Array

def Perform_Analysis(Data_Array, User_Min):
    if User_Min is int:
        User_Min = User_Min
    else:
        User_Min = None

    from ECG_Analysis import ECG
    Object = ECG(Data_Array = Data_Array, User_Min = User_Min)
    Object.Method_Duration()
    Object.Method_Voltage_Extremes()
    Object.Method_Mean_hr_bpm()

    return (Object.Mean_hr_bpm, Object.Duration, Object.Voltage_Extremes, Object.Num_Beats, Object.Beats)

def Save_Results(File_Name_Input, Results):
    from Class_Parse import Parse_Files
    Object = Parse_Files(File_Name = File_Name_Input, Calculations = Results)
    Object.Write_File()

if __name__ == "__main__":
    main()

