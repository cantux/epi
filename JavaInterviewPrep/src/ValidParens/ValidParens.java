package ValidParens;

import java.util.Stack;

public class ValidParens {

    public static void main(String[] args) {
//        System.out.println("result: " + isValid(""));
//        System.out.println("result: " + isValid("(]"));
//        System.out.println("result: " + isValid("{}}"));
//        System.out.println("result: " + isValid("{}[}"));
//        System.out.println("result: " + isValid("{[}"));
        System.out.println("result: " + isValid("({[])"));
    }

    //gotcha
    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }
        return stack.isEmpty();
    }

//    public static boolean isValid(String s) {
//        int count = 0;
//        for(int i = 0; i < s.length(); i++) {
//            char c = s.charAt(i);
//            if(c == '{'
//                    || c == '['
//                    || c == '(') {
//                count++;
//            }
//            else if(c == '}' || c == ']' || c == ')'){
//                count--;
//            }
//            else {
//                return false;
//            }
//        }
//        return count ==0;
//    }
//
//    public static boolean isValid(String s) {
//        return isValid(s, 0, 1);
//    }
//
//    public static boolean isValid(String s, int currentIndex, int nextIndex) {
//        char start = s.charAt(currentIndex);
//        char end = s.charAt(nextIndex);
//        if(currentIndex == nextIndex) {
//            return false;
//        }
//        else if(start == end) {
//            return isValid(s.substring(currentIndex + 1, nextIndex-1), currentIndex, nextIndex-1);
//        }
//        else if()
//
//
//        return false;
//    }


}
