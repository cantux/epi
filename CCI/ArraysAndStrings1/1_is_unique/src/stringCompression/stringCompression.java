package stringCompression;

public class stringCompression {

    public static void main(String[] args) {
        String[] test = {
                "a",
                "abc",
                "aaa",
                "aaaa",
                "aaaabbbb",
                "aaaabbb",
                "aaaabb",
                "aab",
                "aaabb",
                "aabb",
                "aaabbbccc",
                "abccc",
                "abcabcabc"
        };

        for (String a : test) {
            System.out.println("Result for N^2 a: " + a + " is: " + compress(a));
        }
    }

    public static String compress(String str) {
        int i = 0;
        int count = 0;
        String tempString = "";
        while(i < str.length())
        {
            while(i+1 < str.length() && str.charAt(i) == str.charAt(i+1)) {
                count++;
                i++;
            }
            if (count == 1) {
                tempString += "" + str.charAt(i) + str.charAt(i);
                count=0;
            }
            else if(count >= 2) {
                tempString += str.charAt(i) + Integer.toString(count + 1);
                count = 0;
            }
            else
            {
                tempString += str.charAt(i);
            }
            i++;
        }

        return tempString;
    }
}
