package CheckParensValid;

public class CheckParensValidRec {
    public static void main(String[] args) {
        System.out.println("empty" + checkParens(""));
        System.out.println("()" + checkParens("()"));
        System.out.println("()()" + checkParens("()()"));
        System.out.println("(())" + checkParens("(())"));
        System.out.println("(())()" + checkParens("(())()"));
        System.out.println("()(())" + checkParens("()(())"));
        System.out.println("(()())" + checkParens("(()())"));
        System.out.println("((()))" + checkParens("((()))"));

        System.out.println("((()))" + checkParens("("));
        System.out.println("((()))" + checkParens(")"));
        System.out.println("((()))" + checkParens(")("));
        System.out.println("((()))" + checkParens(")()"));
        System.out.println("((()))" + checkParens(")()"));
    }

    public static boolean checkParens(String s) {
        return true;
    }
}
