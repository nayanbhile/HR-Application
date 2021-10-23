from hr import DBConnection, DataLayerException
try:
    sbConnection=DBConnection.getConnection()
    print("Connection established")
except DataLayerException as dataLayerException:
    print(dataLayerException.message)
    print(dataLayerException.exceptions)
finally:
    try:
        if dbConnection.is_connected(): sbConnection.close()
    except:
        pass