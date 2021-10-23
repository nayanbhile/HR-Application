import java.text.*;
class eg3psp
{
public static void main(String dd[])
{
try
{
SimpleDateFormat sdf=new SimpleDateFormat("dd/MM/yy");
java.util.Date date;
date=sdf.parse(dd[0]);
String s=sdf.format(date);	
System.out.println(s);
}catch(Exception e)
{
System.out.println(e);
}
}
}