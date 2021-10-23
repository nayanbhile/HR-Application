from common.hr import Designation
from network_common.wrappers import Request
r1=Request("DesignationManager","getAllDesignations")
str=r1.to_json()
print(str)
print("-"*30)
r2=Request.from_json(str)
print("Manager: ",r2.manager)
print("Action: ",r2.action)
print("JSON String: ",r2.json_string)
print("*"*30)
