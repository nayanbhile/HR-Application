import java.util.*;
class reasspsp
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
int lb=0,ub=list.size(),index=0;
while(ub-lb>1)
{
index=(lb+ub)/2;
int diff=s.compareTo(list.get(index-1));
if(diff>0)
{
lb=index;
}
else
{
ub=index;
}
}
if(s.compareTo(list.get(lb))<0)
{
list.add(lb,s);
}
else
{
list.add(ub,s);
}
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