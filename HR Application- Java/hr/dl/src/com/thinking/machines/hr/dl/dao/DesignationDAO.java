package com.thinking.machines.hr.dl.dao;
import java.io.*;
import java.util.*;
import com.thinking.machines.hr.dl.exceptions.*;
import com.thinking.machines.hr.dl.interfaces.*;
import com.thinking.machines.hr.dl.dto.*;

public class DesignationDAO implements DesignationDAOInterface
{

public void add(DesignationDTOInterface DesignationDTO) throws DAOException
{
try
{
File file=new File(DESIGNATION_DATA_FILE);
int lastGenratedCode=0;
int count=0;
RandomAccessFile randomAccessFile;
randomAccessFile=new RandomAccessFile(file,"rw");
if(randomAccessFile.length()==0) 
{
randomAccessFile.writeBytes("0         \n");
randomAccessFile.writeBytes("0         \n");
}
randomAccessFile.seek(0);
lastGenratedCode=Integer.parseInt(randomAccessFile.readLine().trim());
count=Integer.parseInt(randomAccessFile.readLine().trim());
String vTitle=DesignationDTO.getTitle().trim();
String fTitle;
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
randomAccessFile.readLine();
fTitle=randomAccessFile.readLine();
if(vTitle.equalsIgnoreCase(fTitle))
{
randomAccessFile.close();
throw new DAOException("Designation : "+vTitle +" exists.");
}
}
int vCode;
vCode=lastGenratedCode+1;
randomAccessFile.writeBytes(String.valueOf(vCode));
randomAccessFile.writeBytes("\n");
randomAccessFile.writeBytes(vTitle);
randomAccessFile.writeBytes("\n");
randomAccessFile.seek(0);
String codeString=String.valueOf(vCode);
count++;
String countString=String.valueOf(count);
while(codeString.length()<10) codeString+=" ";
while(countString.length()<10) countString+=" ";
randomAccessFile.writeBytes(codeString+"\n");
randomAccessFile.writeBytes(countString+"\n");
randomAccessFile.close();
DesignationDTO.setCode(vCode);
}catch(IOException ioException)
{
throw new DAOException(ioException.getMessage());
}
}

public void update(DesignationDTOInterface DesignationDTO) throws DAOException
{
int uCode=DesignationDTO.getCode();
String uTitle=DesignationDTO.getTitle();
try
{
boolean found=false;
String fTitle=" ";
int fCode=0;
File file=new File(DESIGNATION_DATA_FILE);
if(!file.exists()) throw new DAOException("Invail Designation code : "+uCode);
RandomAccessFile randomAccessFile=new RandomAccessFile(file,"rw");
if(randomAccessFile.length()==0)
{
randomAccessFile.close();
throw new DAOException("Invail Designation code : "+uCode);
}
//Code To find DesigantionCode
randomAccessFile.seek(0);
randomAccessFile.readLine();
randomAccessFile.readLine();
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
fCode=Integer.parseInt(randomAccessFile.readLine().trim());
randomAccessFile.readLine();
if(fCode==uCode)
{
found=true;
break;
}
}
if(!found)
{
randomAccessFile.close();
throw new DAOException("Invail Designation code : "+uCode);
}

//Checking the Existance of Title
randomAccessFile.seek(0);
randomAccessFile.readLine();
randomAccessFile.readLine();
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
randomAccessFile.readLine();
fTitle=randomAccessFile.readLine().trim();
if(fTitle.equalsIgnoreCase(uTitle))
{
randomAccessFile.close();
throw new DAOException("Title allready exists : "+uTitle);
}
}

randomAccessFile.seek(0);
File tmpFile=new File("falthu.data");
if(tmpFile.exists()) tmpFile.delete();
RandomAccessFile tmpRandomAccessFile=new RandomAccessFile(tmpFile,"rw");
tmpRandomAccessFile.writeBytes(randomAccessFile.readLine()+"\n");
tmpRandomAccessFile.writeBytes(randomAccessFile.readLine()+"\n");
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
fCode=Integer.parseInt(randomAccessFile.readLine().trim());
fTitle=randomAccessFile.readLine().trim();
if(fCode!=uCode)
{
tmpRandomAccessFile.writeBytes(String.valueOf(fCode)+"\n");
tmpRandomAccessFile.writeBytes(fTitle+"\n");
}
else
{
tmpRandomAccessFile.writeBytes(String.valueOf(uCode)+"\n");
tmpRandomAccessFile.writeBytes(uTitle+"\n");
}
}
tmpRandomAccessFile.seek(0);
randomAccessFile.seek(0);
while(tmpRandomAccessFile.getFilePointer()<tmpRandomAccessFile.length())
{
randomAccessFile.writeBytes(tmpRandomAccessFile.readLine()+"\n");
}
randomAccessFile.setLength(tmpRandomAccessFile.length());
tmpRandomAccessFile.setLength(0);
randomAccessFile.close();
tmpRandomAccessFile.close();
}catch(IOException ioException)
{
throw new DAOException(ioException.getMessage());
}
}

public void delete(int code) throws DAOException
{
try
{
boolean found=false;
String fTitle=" ";
int fCode=0;
File file=new File(DESIGNATION_DATA_FILE);
if(!file.exists()) throw new DAOException("Invail Designation code : "+code);
RandomAccessFile randomAccessFile=new RandomAccessFile(file,"rw");
if(randomAccessFile.length()==0)
{
randomAccessFile.close();
throw new DAOException("Invail Designation code : "+code);
}
randomAccessFile.seek(0);
randomAccessFile.readLine();
randomAccessFile.readLine();
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
fCode=Integer.parseInt(randomAccessFile.readLine().trim());
randomAccessFile.readLine();
if(fCode==code)
{
found=true;
break;
}
}
if(!found)
{
randomAccessFile.close();
throw new DAOException("Invail Designation code : "+code);
}
randomAccessFile.seek(0);
File tmpFile=new File("falthu.data");
if(tmpFile.exists()) tmpFile.delete();
RandomAccessFile tmpRandomAccessFile=new RandomAccessFile(tmpFile,"rw");
tmpRandomAccessFile.writeBytes(randomAccessFile.readLine()+"\n");
int count=Integer.parseInt(randomAccessFile.readLine().trim());
count--;
tmpRandomAccessFile.writeBytes(String.valueOf(count)+"\n");
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
fCode=Integer.parseInt(randomAccessFile.readLine().trim());
fTitle=randomAccessFile.readLine().trim();
if(fCode!=code)
{
tmpRandomAccessFile.writeBytes(String.valueOf(fCode)+"\n");
tmpRandomAccessFile.writeBytes(fTitle+"\n");
}
}
tmpRandomAccessFile.seek(0);
randomAccessFile.seek(0);
while(tmpRandomAccessFile.getFilePointer()<tmpRandomAccessFile.length())
{
randomAccessFile.writeBytes(tmpRandomAccessFile.readLine()+"\n");
}
randomAccessFile.setLength(tmpRandomAccessFile.length());
tmpRandomAccessFile.setLength(0);
randomAccessFile.close();
tmpRandomAccessFile.close();
}catch(IOException ioException)
{
throw new DAOException(ioException.getMessage());
}
}

public DesignationDTOInterface getByCode(int code)throws DAOException
{
try
{
File file=new File(DESIGNATION_DATA_FILE);
if(!file.exists()) throw new DAOException("Invalid Designation code : "+code);
RandomAccessFile randomAccessFile=new RandomAccessFile(file,"rw");
if(randomAccessFile.length()==0)
{
randomAccessFile.close();
throw new DAOException("Invalid Designation code : "+code);
}
randomAccessFile.seek(0);
randomAccessFile.readLine();
randomAccessFile.readLine();
DesignationDTOInterface DesignationDTO;
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
int fCode=Integer.parseInt(randomAccessFile.readLine());
String fTitle=randomAccessFile.readLine();
if(fCode==code)
{
randomAccessFile.close();
DesignationDTO=new DesignationDTO();
DesignationDTO.setCode(fCode);
DesignationDTO.setTitle(fTitle);
return DesignationDTO;
}
}
randomAccessFile.close();
throw new DAOException("Invalid Designation Code : "+code);
}catch(IOException ioException)
{
throw new DAOException(ioException.getMessage());
}
}

public DesignationDTOInterface getByTitle(String title)throws DAOException
{
try
{
File file=new File(DESIGNATION_DATA_FILE);
if(!file.exists()) throw new DAOException("Invalid Designation title : "+title);
RandomAccessFile randomAccessFile=new RandomAccessFile(file,"rw");
if(randomAccessFile.length()==0)
{
randomAccessFile.close();
throw new DAOException("Invalid Designation title : "+title);
}
randomAccessFile.seek(0);
randomAccessFile.readLine();
randomAccessFile.readLine();
DesignationDTOInterface DesignationDTO;
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
int fCode=Integer.parseInt(randomAccessFile.readLine());
String fTitle=randomAccessFile.readLine();
if(fTitle.equalsIgnoreCase(title.trim()))
{
randomAccessFile.close();
DesignationDTO=new DesignationDTO();
DesignationDTO.setCode(fCode);
DesignationDTO.setTitle(fTitle);
return DesignationDTO;
}
}
randomAccessFile.close();
throw new DAOException("Invalid Designation title : "+title);
}catch(IOException ioException)
{ 
throw new DAOException(ioException.getMessage());
}
}

public List<DesignationDTOInterface> getAll() throws DAOException
{
List<DesignationDTOInterface> designations;
designations=new LinkedList<DesignationDTOInterface>();
try
{
File file=new File(DESIGNATION_DATA_FILE);
if(!file.exists()) return designations;
RandomAccessFile randomAccessFile=new RandomAccessFile(file,"rw");
if(randomAccessFile.length()==0)
{
randomAccessFile.close();
return designations;
}
randomAccessFile.seek(0);
randomAccessFile.readLine();
randomAccessFile.readLine();
DesignationDTOInterface DesignationDTO;
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
int fCode=Integer.parseInt(randomAccessFile.readLine().trim());
String fTitle=randomAccessFile.readLine();
DesignationDTO=new DesignationDTO();
DesignationDTO.setCode(fCode);
DesignationDTO.setTitle(fTitle);
designations.add(DesignationDTO);
}
return designations;
}catch(IOException ioException)
{
throw new DAOException(ioException.getMessage());
}
}

public int getCount() throws DAOException
{
try
{
File file=new File(DESIGNATION_DATA_FILE);
if(!file.exists()) return 0;
RandomAccessFile randomAccessFile=new RandomAccessFile(file,"rw");
if(randomAccessFile.length()==0) 
{
randomAccessFile.close();
return 0;
}
randomAccessFile.seek(0);
randomAccessFile.readLine();
int count=Integer.parseInt(randomAccessFile.readLine().trim());
randomAccessFile.close();
return count;
}catch(IOException ioException)
{
throw new DAOException(ioException.getMessage());
}
}

public boolean exists(int code) throws DAOException
{
try
{
File file=new File(DESIGNATION_DATA_FILE);
if(!file.exists()) return false;
RandomAccessFile randomAccessFile=new RandomAccessFile(file,"rw");
if(randomAccessFile.length()==0)
{
randomAccessFile.close();
return false;
}
randomAccessFile.seek(0);
randomAccessFile.readLine();
randomAccessFile.readLine();
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
int vCode;
vCode=Integer.parseInt(randomAccessFile.readLine().trim());
randomAccessFile.readLine();
if(code==vCode)
{
randomAccessFile.close();
return true;
}
}
randomAccessFile.close();
return false;
}catch(IOException ioException)
{
throw new DAOException(ioException.getMessage());
}
}

public boolean exists(String title) throws DAOException
{
try
{
File file=new File(DESIGNATION_DATA_FILE);
if(!file.exists()) return false;
RandomAccessFile randomAccessFile=new RandomAccessFile(file,"rw");
randomAccessFile.seek(0);
if(randomAccessFile.length()==0)
{
randomAccessFile.close();
return false;
}
randomAccessFile.readLine();
randomAccessFile.readLine();
while(randomAccessFile.getFilePointer()<randomAccessFile.length())
{
String vTitle;
randomAccessFile.readLine();
vTitle=randomAccessFile.readLine().trim();
if(vTitle.equalsIgnoreCase(title))
{
randomAccessFile.close();
return true;
}
}
randomAccessFile.close();
return false;
}catch(IOException ioException)
{
throw new DAOException(ioException.getMessage());
}
}
}