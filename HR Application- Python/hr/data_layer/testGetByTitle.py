from hr import Designation,DataLayerException,HRDLHandler
import sys
try:
    title=sys.argv[1]
    designation=HRDLHandler.get_designation_by_title(title)
    print("Code: ",designation.code,"    Title: ",designation.title)
except DataLayerException as dataLayerException:
    print(dataLayerException.message)
    print(dataLayerException.exceptions)