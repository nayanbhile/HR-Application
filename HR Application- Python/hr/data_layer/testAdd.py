from hr import Designation,DataLayerException,HRDLHandler
import sys
try:
    title=sys.argv[1]
    designation=Designation(0,title)
    HRDLHandler.add_designation(designation)
    print(f"Designation :{title} added")
except DataLayerException as dataLayerException:
    print(dataLayerException.message)
    print(dataLayerException.exceptions)