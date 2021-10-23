import json
from common.hr import Designation
from network_common.wrappers import Response

# the following is an example of custom exception

class Whatever(Exception):
    def __init__(self,message):
        self.message=message
    def to_json(self):
        return json.dumps(self.__dict__)
    def from_json(json_string):
        new_dict=json.loads(json_string)
        return Whatever(new_dict["message"])

r1=Response(False,error=Whatever("Invalid code 10"))
str=r1.to_json()
print(r1)
print("-"*30)
r2=Response.from_json(str)
print("Success: ",r2.success)
print("Error JSON String: ",r2.error_json_string)
print("Result JSON String: ",r2.result_json_string)
print("="*30)
ex=Whatever(r2.error_json_string)
print(ex.message)