import json
class ValidationException(Exception):
    def __init__(self,message="",exceptions=None):
        self.message=message
        self.exceptions=exceptions
    def to_json(self):
        return json.dumps(self.__dict__)
    def from_json(json_string):
        new_dict=json.loads(json_string)
        return ValidationException(**new_dict)

class Designation:
    def __init__(self,code=0,title="",exceptions={},has_exceptions=False):
        self.exceptions=exceptions
        self.has_exceptions=has_exceptions
        self.code=code
        self.title=title
        self._validate_values()
    def _validate_values(self):
        if isinstance(self.code,int)==False:
            self.exceptions["code"]=('T',f"code is of type: {type(self.code)}, it should be of type: {type(10)}")
        if isinstance(self.title,str)==False:
            self.exceptions["title"]=('T',f"title is of type: {type(self.title)}, it should be of type: {type('D')}")
        if ('code' in self.exceptions)==False and self.code<0:
            self.exceptions["code"]=('V',f"Value of ccode is: {self.code}, it should be >0")
        if ('title' in self.exceptions)==False:
            lengthOfTitle=len(self.title)
            if lengthOfTitle<=0 or lengthOfTitle>35:
                self.exceptions["title"]=('V',f"Length of title is: {lengthOfTitle}, it should be >=1 or  <=35")
        if len(self.exceptions)>0:
            self.has_exceptions=True
    def to_json(self):
        return json.dumps(self.__dict__)
    def from_json(json_string):
        new_dict=json.loads(json_string)
        return Designation(**new_dict)

class HRDLHandler:
    def add_designation(designation):
        pass
    def update_designation(designation):
        pass
    def delete_designation(code):
        pass
    def get_designations():
        pass
    def get_designation_by_code(code):
        pass
    def get_designation_by_title(title):
        pass
    def get_designation_count():
        pass
