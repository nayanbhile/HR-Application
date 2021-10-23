import java.util.*;

class eg1psp
{
public static void main(String d[])
{
List<String> list=new LinkedList<>();
for(int i=0;i<10;i++)
{
String id=UUID.randomUUID().toString();
System.out.println(id);
list.add(id);
}
Collections.sort(list);
System.out.println("-------------Sorted List---------------");
for(int i=0;i<10;i++)
{
System.out.println(list.get(i));
}

}


}