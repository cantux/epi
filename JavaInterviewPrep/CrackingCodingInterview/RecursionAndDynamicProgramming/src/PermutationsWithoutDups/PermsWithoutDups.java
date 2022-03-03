package PermutationsWithoutDups;

import java.util.ArrayList;

public class PermsWithoutDups {
    public static void main(String[] args) {
        System.out.println(getPerms("012"));
        System.out.println(getPerms("0123"));
        System.out.println(getPerms("01234"));
    }

    public static ArrayList<String> getPerms(String s)
    {
        ArrayList<String> result = new ArrayList();
        if(s.length() == 0) {
            result.add("");
            return result;
        }

        for(int i = 0; i < s.length(); i++) {
            char t = s.charAt(i);
            String before = s.substring(0, i);
            String after = s.substring(i+1, s.length());
            ArrayList<String> partials = getPerms(before + after);

            for(String elem: partials) {
                result.add(t + elem);
            }
        }

        return result;
    }
}
