package ReverseOrderOfWords;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ReverseOrderOfWords {
    public static void main(String[] args) {
//        char[] sentence = new char[]{'a', 'a','a', ' ', 'b', 'b', 'b'};
//
//        System.out.println(reverseOrder(sentence));

//        char[] sentence1 = new char[]{'a'};
//
//        System.out.println(reverseOrder(sentence1));
//
//        char[] sentence2 = new char[]{};
//
//        System.out.println(reverseOrder(sentence2));
//
//        char[] sentence3 = new char[]{'a', ' ', 'b'};
//
//        System.out.println(reverseOrder(sentence3));

        System.out.println("Some deeds can not be reversed" + reverseSentenceWords("Some deeds can not be reversed"));
    }

    public static String reverseSentenceWords(String s) {
        String[] sArr = s.split(" ");
        ArrayList<String> sList = new ArrayList<>(Arrays.asList(sArr));

        ArrayList a = reverArr(sList);
        return a.toString();
    }
    public static ArrayList reverArr(ArrayList arr) {
        ArrayList newArr = new ArrayList();
        reverseArrHelper(arr, 0, arr.size(), newArr);
        return newArr;
    }

    public static void reverseArrHelper(ArrayList arr, int current, int size, ArrayList newArr) {
        if(current == size) {
            return;
        }
        reverseArrHelper(arr, current + 1, size, newArr);

        newArr.add(arr.get(current));
    }

    // awesome solution, reverse individual words then reverse whole sting viola.....

    public static char[] reverseOrder(char[] sentenceCharArray) {
        // create word strings

        ArrayList<ArrayList<Character>> wordArr = new ArrayList<>();

        // walk through every character, saving it into an array
        ArrayList<Character> tempCharArray = new ArrayList<>();
        for(int i = 0; i< sentenceCharArray.length; i++) {
            if(sentenceCharArray[i] == ' ') {
                wordArr.add(tempCharArray);

                tempCharArray = new ArrayList<>();
            }
            else {
                tempCharArray.add(sentenceCharArray[i]);
            }
        }
        wordArr.add(tempCharArray);

        // reverse order recursively or via a loop
        ArrayList a = reverArr(wordArr);
        return fromArrayListToCharArray(a);

    }

    public static void reverseArrayList(ArrayList arr) {
        Collections.reverse(arr);
    }

    public static char[] fromArrayListToCharArray(ArrayList<ArrayList<Character>> chArr) {
        int totalSize = 0;
        for(ArrayList<Character> wordCh: chArr) {
            totalSize += wordCh.size();
        }

        char[] sentenceArr = new char[totalSize];

        int i = 0;
        for(ArrayList<Character> wordCh: chArr) {
            for(char c: wordCh) {
                sentenceArr[i] = c;
                i++;
            }
        }
        return sentenceArr;
    }
}
