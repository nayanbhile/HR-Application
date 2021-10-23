class City
{
}
class testpsp
{
private static enum GENDER{MALE,FEMALE};
public int rollNumber;
public int phNo;
public String name;
public String fatherName;
public String motherName;
public boolean isIndian;
public GENDER gender;
public int age;
public City city;


public testpsp()
{
this.rollNumber=0;
this.phNo=0;
this.name="";
this.fatherName="";
this.motherName="";
this.isIndian=false;
this.gender=null;
this.age=0;
this.city=null;
}
public void setRollNumber(int rollNumber)
{
this.rollNumber=rollNumber;
}
public int getRollNumber()
{
return this.rollNumber;
}
public void setPhNo(int phNo)
{
this.phNo=phNo;
}
public int getPhNo()
{
return this.phNo;
}
public void setName(java.lang.String name)
{
this.name=name;
}
public java.lang.String getName()
{
return this.name;
}
public void setFatherName(java.lang.String fatherName)
{
this.fatherName=fatherName;
}
public java.lang.String getFatherName()
{
return this.fatherName;
}
public void setMotherName(java.lang.String motherName)
{
this.motherName=motherName;
}
public java.lang.String getMotherName()
{
return this.motherName;
}
public void setIsIndian(boolean isIndian)
{
this.isIndian=isIndian;
}
public boolean getIsIndian()
{
return this.isIndian;
}
public void setGender(testpsp$GENDER gender)
{
this.gender=gender;
}
public testpsp$GENDER getGender()
{
return this.gender;
}
public void setAge(int age)
{
this.age=age;
}
public int getAge()
{
return this.age;
}
public void setCity(City city)
{
this.city=city;
}
public City getCity()
{
return this.city;
}

}