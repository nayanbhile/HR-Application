import java.awt.datatransfer.*;
import java.awt.*;

class psp
{
public static void main(String dd[])
{
String a="God is great. Ujjain is city of GODS";
StringSelection ss=new StringSelection(a);
Clipboard clipboard;
clipboard=Toolkit.getDefaultToolkit().getSystemClipboard();
clipboard.setContents(ss,ss);
}
}