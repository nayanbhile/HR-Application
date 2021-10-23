from hr import Designation,DataLayerException,HRDLHandler
import sys
try:
    code=int(sys.argv[1])
    HRDLHandler.delete_designation(code)
    print(f"Designation deleted")
except DataLayerException as dataLayerException:
    print(dataLayerException.message)
    print(dataLayerException.exceptions)