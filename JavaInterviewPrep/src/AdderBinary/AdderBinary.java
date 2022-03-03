package AdderBinary;

import java.util.Arrays;

public class AdderBinary {
    public static void main(String[] args) {
//        System.out.println("result: " + addBinary("111", "111"));
//        System.out.println("result: " + addBinary("11", "1"));
//        System.out.println("result: " + addBinary("1010", "1011"));
        System.out.println("result: " + addBinary("100", "110010"));

    }

    public static String addBinary(String a, String b) {
        if(a == null || a.isEmpty()) {
            return b;
        }
        if(b == null || b.isEmpty()) {
            return a;
        }

        int aLength = a.length();
        int bLength = b.length();

        StringBuilder s = new StringBuilder();
        // go till the shorter is finished
        int carry = 0;
        int i = aLength - 1, j = bLength - 1;
        while(i >= 0 || j >= 0) {
            int sum = carry;
            if (j >= 0) sum += b.charAt(j--) - '0';
            if (i >= 0) sum += a.charAt(i--) - '0';
            s.append(sum % 2);
            carry = sum / 2;
        }

        // if still carry left added to the last
        if(carry == 1) s.append('1');

        return s.reverse().toString(); // return reverse of the built binary.
    }
}
