#The main function that will call all the others


try:
    import logging
except ImportError:
    print("Could not import logging")

try:
    import sphinx
except ImportError:
    print("Could not import sphinx")

def main():
    File_Name_Input = input("What is the name of the file containing the ECG data?")

    Data_Array = Get_File(File_Name_Input)
    Results = Perform_Analysis(Data_Array)
    Save_Results(Results)


def Get_File(File_Name_Input):
    from Class_Parse import Parse_Files
    Object = Parse_Files(File_Name = File_Name_Input, Calculations = None)
    Object.Read_File()

    Data_Array = Object.Data_Array

    return Data_Array

def Perform_Analysis(Data_Array):
    from ECG_Analysis import ECG
    Object = ECG(Data_Array = Data_Array)
    Object.Method_Duration()
    Object.Method_Voltage_Extremes()
    
    print(Object.Duration)
    print(Object.Voltage_Extremes)
    
    Results = Object.Duration
    return Results

def Save_Results(Results):
    pass

if __name__ == "__main__":
    main()

