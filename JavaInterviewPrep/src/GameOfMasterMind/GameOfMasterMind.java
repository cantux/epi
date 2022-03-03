package GameOfMasterMind;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Result {
    public int hits = 0, pseudoHits = 0;
    public String toString() {
        return "hits: " + hits + " pseudohits: " + pseudoHits;
    }
}
public class GameOfMasterMind {
    public static void main(String[] args) {
        Result r = solve("RGGB", "YRGB");
        System.out.println("result: " + r);
        List<String> list = new ArrayList<>();
        genArrays(4, new char[0], list);
        System.out.println("lists: " + list);
    }

    public static char[] letters = new char[] {'R', 'G', 'B', 'Y'};
    public static void genArrays(int size, char[] current, List<String> list) {
        if(size == current.length) {
            list.add(String.valueOf(current));
            return;
        }

        char[] newArr = new char[current.length + 1];
        for(int j = 0; j < current.length; j++) {
            newArr[j] = current[j];
        }

        for(int i = 0; i < letters.length; i++) {
            newArr[current.length] = letters[i];
            genArrays(size, newArr, list);
        }
    }

    // correct color, correct spot, exact hit
    // correct color, wrong spot, pseudo hit
    public static Result solve(String guess, String solution) {
        // exact hit is a subset of pseduo hit so I think first we should remove all the exact hits
        // then move on to check for pseduo hits

        Result r = new Result();
        // length checks -> if they are exact length, if they have length larger than 0.

        Map<Character, Integer> guessFreqMap = new HashMap();
        Map<Character, Integer> solFreqMap = new HashMap();
        for(int i = 0; i < guess.length(); i++) {
            char gChar = guess.charAt(i);
            char sChar = solution.charAt(i);

            if(gChar != sChar) {
                guessFreqMap.put(gChar, guessFreqMap.getOrDefault(gChar, 0) + 1);
                solFreqMap.put(sChar, solFreqMap.getOrDefault(gChar, 0) + 1);

            }
            else {
                r.hits++;
            }
        }

        for(Map.Entry<Character,Integer> ent: guessFreqMap.entrySet()) {
            r.pseudoHits += Math.min(ent.getValue(), solFreqMap.getOrDefault(ent.getKey(), 0));
        }

        return r;
    }
}
