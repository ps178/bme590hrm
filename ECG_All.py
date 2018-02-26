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

    Get_File(File_Name_Input)
    Perform_Analysis(Data_Array)
    Save_Results()


def Get_File():
    pass
    from Class_Parse import Parse_Files
    Object = Parse_Files(File_Name = File_Name_Input)
    Data_Array = Object.Data_Array
    return Data_Array

def Perform_Analysis():
    pass

def Save_Results():
    pass
