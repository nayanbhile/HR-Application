from hr import Designation,DataLayerException,HRDLHandler
import sys
try:
    designations=HRDLHandler.get_designations()
    for designation in designations:
        print("Code: ",designation.code,"    Title: ",designation.title)
except DataLayerException as dataLayerException:
    print(dataLayerException.message)
    print(dataLayerException.exceptions)