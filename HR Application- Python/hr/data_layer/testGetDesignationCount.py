from hr import Designation,DataLayerException,HRDLHandler
import sys
try:
    designationCount=HRDLHandler.get_designation_count()
    print("Designation count: ",designationCount)
except DataLayerException as dataLayerException:
    print(dataLayerException.message)
    print(dataLayerException.exceptions)