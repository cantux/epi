package NumWaysDecodeMessage;

import java.util.HashMap;
import java.util.Map;

public class NumWaysDecodeMessage {

    public static void main(String[] args) {
        Map<Character, Integer> map = new HashMap();
        for(int i = 0; i < 26; i++) {
            map.put((char) (97+i), i +1);
        }
        numDecodings("123");
        System.out.println("count is: " + b.count);
    }

    static Box b = new Box();
    public static int numDecodings(String s) {
        numDecodings(s, s.length());
        return b.count;
    }

    public static boolean numDecodings(String s, int length) {
        System.out.println("s is: " + s);
        if(s.length() == 1) {
            return false;
        }
        else if(s.length() == 2) {
            System.out.println("first char is: " + (int)s.charAt(0) + "second char is: " + (int)s.charAt(1));
            if((int)s.charAt(0) <= 50 && (int)s.charAt(1) <= 55) {
                return true;
            }
            else {
                return false;
            }
        }
        else {
            boolean first = numDecodings(s.substring(1), length - 1);
            boolean second = numDecodings(s.substring(2), length - 2);
            System.out.println("first: " + first + " second: " + second);
            if(first && second) {
                b.count++;
                return true;
            }
            else if(first || second) {
                return true;
            }
        }
        return false;
    }

    public static class Box {
        public int count = 1;
    }

}
