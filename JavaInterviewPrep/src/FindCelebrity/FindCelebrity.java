package FindCelebrity;

import java.util.ArrayList;
import java.util.List;

public class FindCelebrity {

    // Person with 2 is celebrity
    static int MATRIX[][] = { { 0, 0, 1, 0 },
            { 0, 0, 1, 0 },
            { 0, 0, 0, 0 },
            { 0, 0, 1, 0 } };

    // Returns true if a knows
    // b, false otherwise
    static boolean knows(int a, int b)
    {
        return MATRIX[a][b] == 1;
    }

    // Driver Code
    public static void main(String[] args)
    {
        int n = 4;
        int result = findCelebrity(n);
        System.out.println(findCelebrityDP(n));
        if (result == -1)
        {
            System.out.println("No Celebrity");
        }
        else
            System.out.println("Celebrity ID " +
                    result);
    }


    // if there are two people that doesn't know anyone in the party,
    // there can't be a celebrity

    // kth person is the celebrity,

    // people until the kth either knows someone or unknown by someone

    // people after the kth are not known by the kth
    public static int findCelebrityDP(int n) {
        int celeb = 0;
        for(int i = 1; i < n; i++) {
            if(knows(celeb, i)) {
                celeb = i;
            }
        }

        // check to see if the candidate celeb knows anyone
        // or is unknown by everyone else
        for(int i = 0; i < n; i++){
            if(i != celeb)
                if(knows(celeb, i) || !knows(i, celeb)) {
                    return -1;
                }
        }

//        for(int i = 0; i < n; i++){
//            if(i != celeb)
//                if(knows(celeb, i) || !knows(i, celeb)) {
//                    return -1;
//                }
//        }
        return celeb;
    }

    public static int findCelebrity(int n) {
        // brute force solution
        // create a list(or some data structure) to
        // find people that are known by everyone

        // but there is a problem here, no two people can be known by everyone
        // if that's the case there is no celebrity
        // so check the size of the data structure to be exactly equal to 1

        //
        List<Integer> l = new ArrayList();

        for(int i =0; i < n; i++) {
            boolean chosen = true;
            for(int j = 0; j < n; j++) {
                if(j == i) continue;
                chosen &= knows(j, i);
            }
            if(chosen) {
                l.add(i);
            }
        }

        System.out.println("list: " + l);
        boolean knowsNoOne = false;
        for(int celeb: l) {
            for(int k = 0; k < n; k++) {
                if(k == celeb) continue;
                knowsNoOne |= knows(celeb, k);
            }
            if(!knowsNoOne) return celeb;
        }
        return -1;
    }


    public static int findCelebrityOpt(int n) {
        // brute force solution
        // create a list(or some data structure) to find people that are known by everyone
        //
        List<Integer> l = new ArrayList();

        for(int i =0; i < n; i++) {
            boolean chosen = true;
            boolean knowsNoOne = false;
            for(int j = 0; j < n; j++) {
                if(j == i) continue;
                chosen &= knows(j, i);
                knowsNoOne |= knows(i, j);
            }
            if(chosen && !knowsNoOne) {
                l.add(i);
            }
        }

        if(l.size() != 1) {
            return -1;
        }
        return l.get(0);
//        System.out.println("list: " + l);
//        boolean knowsNoOne = false;
//        for(int celeb: l) {
//            for(int k = 0; k < n; k++) {
//                if(k == celeb) continue;
//                knowsNoOne |= knows(celeb, k);
//            }
//            if(!knowsNoOne) return celeb;
//        }
//        return -1;
    }
}
