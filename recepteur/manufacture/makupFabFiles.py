#!/bin/python

from os import path, getcwd, linesep
import re


files = {
        #"BOM" : None,
        "POS" : "recepteur-all-pos.csv",
        }

location = getcwd()+"/"

def checkIfAllFileAreThere()->bool:
    print("Check is POS file exist (",location+files["POS"],") : ",end="")
    if (path.isfile(location+files["POS"])):
        print("OK")
    else : return False

    return True

def updatePOSFile(pathTo:str)->bool:
    print("Updating POS file : ", end="")

    POSFile = []
    with open(pathTo, "r") as file:
        POSFile = [line for line in file]

    # result   =        search / replacment ; source
    POSFile[0] = re.sub("Ref" , "Designator", POSFile[0])
    POSFile[0] = re.sub("PosX", "Mid X"     , POSFile[0])
    POSFile[0] = re.sub("PosY", "Mid Y"     , POSFile[0])
    POSFile[0] = re.sub("Rot" , "Rotation"  , POSFile[0])
    POSFile[0] = re.sub("Side", "Layer"     , POSFile[0])
            
    with open(pathTo, "w") as file:
        for line in POSFile:
            file.write(line)

    print("OK")

    return True

def main():
    if (not checkIfAllFileAreThere()):
        print("ERROR : missing file")
        exit(-1)

    print("\nUpdating files :")
    if (not updatePOSFile(location+files["POS"])):
        print("One file failed to be updated : aborting")
        exit(-1)

    
    print("\nConverting success : Files are ready for manufacturing !")

if __name__=="__main__":
    main()




# Rules list :
#
# BOM : use JLCPBC BOM format in kicad !
#
# POS file : (placement file)
# |-> Column : change Ref to Designator ; PosX to Mid X ; Pos
