import java.util.*;
class assignmentpsp
{
public static void main(String dd[])
{
long startTime=System.currentTimeMillis();
List<String> list=new LinkedList<>();
for(int i=0;i<18000;i++)
{
String s=UUID.randomUUID().toString();
System.out.println(s);
if(list.isEmpty())
{
list.add(s);
}
else
{
int k=0;
for(int j=0;j<list.size()-1;j++,k++)
{
String ss=list.get(j);
int diff=s.compareTo(ss);
if(diff<0)
{
break;
}
}
list.add(k,s);
}
}
System.out.println("-----------Sorted List of UUID--------------");
for(int i=0;i<list.size();i++)
{
System.out.println(list.get(i));
}
long endTime=System.currentTimeMillis();
System.out.println(endTime-startTime);
}
}