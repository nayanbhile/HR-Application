from hr import Designation,DataLayerException,HRDLHandler
import sys
try:
    code=int(sys.argv[1])
    title=sys.argv[2]
    designation=Designation(code,title)
    HRDLHandler.update_designation(designation)
    print(f"Designation: {title} updated")
except DataLayerException as dataLayerException:
    print(dataLayerException.message)
    print(dataLayerException.exceptions)