from tmcomponents.components import Menu
from network_common.wrappers import Request,Response
from network_client.client import NetworkClient
from common.hr import Designation,ValidationException

class HRClientUI:
    def __init__(self):
        pass
    def add_designation(self):
        title=input("Enter designation to be added: ")
        designation=Designation(0,title)
        request=Request(manager="DesignationManager",action="add",request_object=designation)
        network_client=NetworkClient()
        response=network_client.send(request)
        if response.success:
            print("Designation added")
        else:
            validationException=ValidationException.from_json(response.error_json_string)
            if validationException.message and len(validationException.message)>0: print(validationException.message)
            if validationException.exceptions:
                for exception in validationException.exceptions.values():
                    print(exception[1])

def main_menu_handler(menu,choice):
    if choice==1: designation_menu.activate()
    if choice==2: employee_menu.activate()
    if choice==3: menu.deactivate()

def designation_menu_handler(menu,choice):
    if choice==1:
        hr_client_ui=HRClientUI()
        hr_client_ui.add_designation()
    if choice==6: menu.deactivate()

def employee_menu_handler(menu,choice):
    if choice==6: menu.deactivate()

main_menu=Menu("Main menu",main_menu_handler)
main_menu.add_option("Designation Master")
main_menu.add_option("Employee Master")
main_menu.add_option("Exit")

designation_menu=Menu("Designation Master",designation_menu_handler)
designation_menu.add_option("Add")
designation_menu.add_option("Edit")
designation_menu.add_option("Delete")
designation_menu.add_option("Search")
designation_menu.add_option("Display List")
designation_menu.add_option("Exit")

employee_menu=Menu("Employee Master",employee_menu_handler)
employee_menu.add_option("Add")
employee_menu.add_option("Edit")
employee_menu.add_option("Delete")
employee_menu.add_option("Search")
employee_menu.add_option("Display List")
employee_menu.add_option("Exit")

main_menu.activate()