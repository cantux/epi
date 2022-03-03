package LookAndSay;

import java.util.ArrayList;
import java.util.List;

public class LookAndSay {

    public static void main(String[] args) {
        System.out.println(loop(10));
    }

    public static List<String> loop(int times) {
        String s = "";
        List<String> sList = new ArrayList();
        for(int i = 0; i < times; i++) {
            sList.add(s);
            s = lookAndSay(s);
        }

        return sList;
    }

    public static String lookAndSay(String s) {
        if(s.length() < 1) {
            return "1";
        }

        char[] arr = s.toCharArray();
        String returnS = "";
        int i = 1, count = 1;
        while(i < arr.length) {
            if(arr[i] == arr[i - 1]) {
                count++;
            }
            else {
                returnS += count + "" + arr[i - 1];
                count = 1;
            }
            i++;
        }
        returnS += count + "" + arr[i - 1];
        return returnS;
    }
}
