from os import path
from xml.etree import ElementTree
from mysql.connector import connect,Error

class DataLayerException(Exception):
    def __init__(self,message="",exceptions=None):
        self.message=message
        self.exceptions=exceptions

class DBConfiguration:
    def __init__(self,host,port,database,user,password):
        self.exceptions=dict()
        self.has_exceptions=False
        self.host=host
        self.port=port
        self.database=database
        self.user=user
        self.password=password
        self._validate_values()
    def _validate_values(self):
        if isinstance(self.host,str)==False:
            self.exceptions["host"]=('T',f"Host is of type: {type(self.host)}, it should be of type: {type('A')}")
        if isinstance(self.port,int)==False:
            self.exceptions["port"]=('T',f"Port is of type: {type(self.port)}, it should be of type: {type(10)}")
        if isinstance(self.database,str)==False:
            self.exceptions["database"]=('T',f"Database is of type: {type(self.database)}, it should be of type: {type('A')}")
        if isinstance(self.user,str)==False:
            self.exceptions["user"]=('T',f"User is of type: {type(self.user)}, it should be of type: {type('A')}")
        if isinstance(self.password,str)==False:
            self.exceptions["password"]=('T',f"Password is of type: {type(self.password)}, it should be of type: {type('A')}")

        if ('host' in self.exceptions)==False and len(self.host)==0:
            self.exceptions["host"]=('V',"Missing host/ip name")
        if ('port' in self.exceptions)==False and (self.port<=0 or self.port>=65535):
            self.exceptions["port"]=('V',f"Port is {self.port}, it should be >=1 or <=65535")
        if ('databse' in self.exceptions)==False and len(self.database)==0:
            self.exceptions["database"]=('V',"Missing database name")
        if ('user' in self.exceptions)==False and len(self.user)==0:
            self.exceptions["user"]=('V',"Missing user")
        if ('password' in self.exceptions)==False and len(self.password)==0:
            self.exceptions["hpassword"]=('V',"Missing password")
        if len(self.exceptions)>0:
            self.has_exceptions=True

class DBUtility:
    def getDBConfiguration():
        if path.isfile("dbconfig.xml")==False:
            raise DataLayerException("dbconfig.xml with database connection details is missing, refer to documentation")
        f=open("dbconfig.xml","r")
        try:
            xmlTree=ElementTree.parse(f)
        except:
            raise DataLayerException("Contents of dbconfig.xml ate malformed")
        finally:
            f.close()
        rootNode=xmlTree.getroot()
        host=None
        port=None
        database=None
        user=None
        password=None
        for node in rootNode:
            if node.tag=="host": host=node.text
            if node.tag=="port": port=node.text
            if node.tag=="name": database=node.text
            if node.tag=="user": user=node.text
            if node.tag=="password": password=node.text
        if port!=None:
            try:
                p=int(port)
            except:
                raise DataLayerException(f"Port in dbconfig.xml is of type: {type(port)}, it should be of type: {type(10)}")
        return DBConfiguration(host,int(port),database,user,password)

class DBConnection:
    def getConnection():
        dbConfiguration=DBUtility.getDBConfiguration()
        if dbConfiguration.has_exceptions: raise DataLayerException(dbConfiguration.exceptions)
        try:
            connection=connect(host=dbConfiguration.host,port=dbConfiguration.port,database=dbConfiguration.database,user=dbConfiguration.user,password=dbConfiguration.password)
        except Error as error:
            raise DataLayerException(error.msg)
        return connection

class Designation:
    def __init__(self,code,title):
        self.exceptions=dict()
        self.has_exceptions=False
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
class HRDLHandler:
    def add_designation(designation):
        if designation==None: raise DataLayerException("Designation required")
        if isinstance(designation,Designation)==False: raise DataLayerException(f"type <class Designation> required, found type {type(designation)}")
        if designation.has_exceptions: raise DataLayerException(exceptions=designation.exceptions)
        if designation.code!=0: raise DataLayerException("Designation code should be equal to 0 as it will be auto generated")
        try:
            dbConnection=DBConnection.getConnection()
            cursor=dbConnection.cursor()
            cursor.execute("select code from designation where title=%s",(designation.title,))
            rows=cursor.fetchall()
            if len(rows)>0: raise DataLayerException(f"{designation.title} exists")
            cursor.execute("insert into designation (title) values (%s)",(designation.title,))
            designation.code=cursor.lastrowid
            dbConnection.commit()
        except Error as error:
            raise DataLayerException(error.msg)
        finally:
            try:
                if cursor.is_open(): cursor.close()
                if dbConnection.is_connected(): dbConnection.close()
            except:
                pass


    def update_designation(designation):
        if designation==None: raise DataLayerException("Designation required")
        if isinstance(designation,Designation)==False: raise DataLayerException(f"type <class Designation> required, found type {type(designation)}")
        if designation.has_exceptions: raise DataLayerException(exceptions=designation.exceptions)
        if designation.code==0: raise DataLayerException("Designation code can not be equal to 0")
        try:
            dbConnection=DBConnection.getConnection()
            cursor=dbConnection.cursor()
            cursor.execute("select code from designation where code=%s",(designation.code,))
            rows=cursor.fetchall()
            if len(rows)==0: raise DataLayerException("Code: {designation.code} doesn't exist")
            cursor.execute("select code from designation where title=%s and code<>%s",(designation.title,designation.code))
            rows=cursor.fetchall()
            if len(rows)>0: raise DataLayerException(f"{designation.title} exists")
            cursor.execute("update designation set title=%s where code=%s",(designation.title,designation.code))
            dbConnection.commit()
        except Error as error:
            raise DataLayerException(error.msg)
        finally:
            try:
                if cursor.is_open(): cursor.close()
                if dbConnection.is_connected(): dbConnection.close()
            except:
                pass

    def delete_designation(code):
        if code<=0: raise DataLayerException("Code cannot be less than or equal to 0")
        try:
            dbConnection=DBConnection.getConnection()
            cursor=dbConnection.cursor()
            cursor.execute("select code from designation where code=%s",(code,))
            rows=cursor.fetchall()
            if len(rows)==0: raise DataLayerException("Code: {code} doesn't exist")
            cursor.execute("delete from designation where code=%s",(code,))
            dbConnection.commit()
        except Error as error:
            raise DataLayerException(error.msg)
        finally:
            try:
                if cursor.is_open(): cursor.close()
                if dbConnection.is_connected(): dbConnection.close()
            except:
                pass



    def get_designations():
        designations=list()
        try:
            dbConnection=DBConnection.getConnection()
            cursor=dbConnection.cursor()
            cursor.execute("select * from designation order by title")
            rows=cursor.fetchall()
            for row in rows:
                designation=Designation(row[0],row[1])
                designations.append(designation)
            dbConnection.commit()
        except Error as error:
            raise DataLayerException(error.msg)
        finally:
            try:
                if cursor.is_open(): cursor.close()
                if dbConnection.is_connected(): dbConnection.close()
            except:
                pass
        return designations



    def get_designation_by_code(code):
        try:
            dbConnection=DBConnection.getConnection()
            cursor=dbConnection.cursor()
            cursor.execute("select * from designation where code=%s",(code,))
            rows=cursor.fetchall()
            if len(rows)==0: raise DataLayerException(f"Designation with code: {code} doesn't exist")
            for row in rows:
                designation=Designation(row[0],row[1])
            dbConnection.commit()
        except Error as error:
            raise DataLayerException(error.msg)
        finally:
            try:
                if cursor.is_open(): cursor.close()
                if dbConnection.is_connected(): dbConnection.close()
            except:
                pass
        return designation



    def get_designation_by_title(title):
        try:
            dbConnection=DBConnection.getConnection()
            cursor=dbConnection.cursor()
            cursor.execute("select * from designation where title=%s",(title,))
            rows=cursor.fetchall()
            if len(rows)==0: raise DataLayerException(f"Designation with title: {title} doesn't exist")
            for row in rows:
                designation=Designation(row[0],row[1])
            dbConnection.commit()
        except Error as error:
            raise DataLayerException(error.msg)
        finally:
            try:
                if cursor.is_open(): cursor.close()
                if dbConnection.is_connected(): dbConnection.close()
            except:
                pass
        return designation



    def get_designation_count():
        numberOfDesignations=0
        try:
            dbConnection=DBConnection.getConnection()
            cursor=dbConnection.cursor()
            cursor.execute("select count(*) as cnt from designation")
            row=cursor.fetchone()
            numberOfDesignations=row[0]
            dbConnection.commit()
        except Error as error:
            raise DataLayerException(error.msg)
        finally:
            try:
                if cursor.is_open(): cursor.close()
                if dbConnection.is_connected(): dbConnection.close()
            except:
                pass
        return numberOfDesignations
