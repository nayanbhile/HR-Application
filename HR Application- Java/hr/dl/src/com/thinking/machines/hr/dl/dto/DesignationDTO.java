package com.thinking.machines.hr.dl.dto;
import com.thinking.machines.hr.dl.interfaces.*;
public class DesignationDTO implements DesignationDTOInterface
{
private int code;
private String title;

public void setCode(int code)
{
this.code=code;
}

public int getCode()
{
return this.code;
}

public void setTitle(String title)
{
this.title=title;
}

public String getTitle()
{
return this.title;
}

public int hashCode()
{
return code;
}

public boolean equals(Object object)
{
if(!(object instanceof DesignationDTOInterface)) return false;
DesignationDTOInterface DesignationDTO=(DesignationDTOInterface)object;
return this.code==DesignationDTO.getCode();
}

public int compareTo(DesignationDTOInterface DesignationDTO)
{
return this.code-DesignationDTO.getCode();
}

}