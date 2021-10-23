from network_server.server import NetworkServer
from network_common.wrappers import Request,Response
from common.hr import Designation,ValidationException
import data_layer.hr

def requestHandler(request):
    if request.manager=="DesignationManager":
        if request.action=="add":
            designation=Designation.from_json(request.json_string)
            if designation.has_exceptions:
                validationException=ValidationException("",designation.exceptions)
                response=Response(success=False,error=validationException)
                return response
            dlDesignation=data_layer.hr.Designation(designation.code,designation.title)
            if dlDesignation.has_exceptions:
                validationException=ValidationException("",dlDesignation.exceptions)
                response=Response(success=False,error=validationException)
                return response
            try:
                data_layer.hr.HRDLHandler.add_designation(dlDesignation)
                response=Response(success=True)
                return response
            except data_layer.hr.DataLayerException as dataLayerException:
                validationException=ValidationException(dataLayerException.message,dataLayerException.exceptions)
                response=Response(success=False,error=validationException)
                return response

network_server=NetworkServer(requestHandler)
network_server.start()