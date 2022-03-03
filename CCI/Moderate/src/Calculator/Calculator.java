package Calculator;

public class Calculator {
    public static void main(String[] args) {
        try {
            System.out.println("3+4*2 is: " + execExp("3+4*2"));
            System.out.println("3*4+2 is: " + execExp("3*4+2"));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static int execExp(String exp) throws Exception {

        // exp = value lowPres exp | exp highPres value
        int length = exp.length();
        if(length % 2 != 1) throw new Exception();

        if(exp.length() == 1) {
            return Integer.valueOf(exp);
        }

        int currentIntVal = Integer.parseInt(String.valueOf(exp.charAt(0)));
        char currentOp = exp.charAt(1);

        String rest = exp.substring(2);
        if(currentOp == '*') {
            return currentIntVal * execExp(rest);
        }
        else if(currentOp == '/') {
            return currentIntVal / execExp(rest);
        }
        else if(currentOp == '-') {
            return execExp(rest) - currentIntVal;
        }
        return execExp(rest) + currentIntVal;
    }
}
