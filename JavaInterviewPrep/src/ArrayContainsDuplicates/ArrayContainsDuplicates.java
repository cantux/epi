package ArrayContainsDuplicates;

import java.util.HashSet;
import java.util.Set;

public class ArrayContainsDuplicates {
    public static void main(String[] args) {
        int[] a0 = new int[]{1,2,3,4};
        System.out.println("result0: " + containsDuplicates(a0));


        int[] a1 = new int[]{1,2,3,1};
        System.out.println("result0: " + containsDuplicates(a1));
        int[] a2 = new int[]{1,1};
        System.out.println("result0: " + containsDuplicates(a2));

        int[] a3 = new int[]{};
        System.out.println("result0: " + containsDuplicates(a3));
    }

    public static boolean containsDuplicates(int[] arr) {
        Set<Integer> s = new HashSet();
        for(int i = 0; i < arr.length; i++) {
            if(!s.contains(arr[i])) {
                s.add(arr[i]);
            }
            else {
                return true;
            }
        }
        return false;
    }
}
