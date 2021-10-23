class aaa
{
}

class bbb
{
}

class eg4psp
{
public static void main(String dd[])
{
Class c;
Class b;
c=aaa.class;
b=bbb.class;
String name=c.getName();
String name1=b.getName();
System.out.println("N1 : "+name+"N2 "+name1);

if(name.equals("long") || name.equals("int") || name.equals("float") || name.equals("double") || name.equals("char") || name.equals("short") || name.equals("boolean") || name.equals("byte") || name.equals("String"))
{
System.out.println("1. POJOCopier Called ");
}
else
{
Class c1,c2;
c1=c.getClass();
c2=b.getClass();
System.out.println("1. "+c1);
System.out.println("2. "+c2);
}
System.out.println("3. "+c.getName());
}
}