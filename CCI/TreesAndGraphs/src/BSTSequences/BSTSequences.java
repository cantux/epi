package BSTSequences;

import Tree.BinaryTree;

import java.util.ArrayList;
import java.util.LinkedList;

public class BSTSequences {
    public static void main(String[] args) {

    }

    public static ArrayList<LinkedList<Integer>> allSequences(BinaryTree<Integer> node){
        ArrayList<LinkedList<Integer>> result = new ArrayList<>();

        if(node == null) {
            result.add(new LinkedList<Integer>());
            return result;
        }

        LinkedList<Integer> prefix = new LinkedList<>();
        prefix.add(node.data);

        ArrayList<LinkedList<Integer>> leftSeq = allSequences(node.left);
        ArrayList<LinkedList<Integer>> rightSeq = allSequences(node.right);

        for(LinkedList<Integer> left: leftSeq) {
            for(LinkedList<Integer> right: rightSeq) {
                ArrayList<LinkedList<Integer>> weaved = new ArrayList();
                weaveLists(left, right, weaved, prefix);
                result.addAll(weaved);
            }
        }

        return result;
    }

    public static void weaveLists(LinkedList<Integer> first, LinkedList<Integer> second,
                    ArrayList<LinkedList<Integer>> results, LinkedList<Integer> prefix) {
        // if one of the lists is empty, Add remainder to prefix and store result
        if(first.size() == 0 || second.size() == 0) {
            LinkedList<Integer> result = (LinkedList<Integer>) prefix.clone();
            result.addAll(first);
            result.addAll(second);
            results.add(result);
            return;
        }

        /** Recurse with head of tfirst added to the prefix. Removing the head will damage first,
         *  so we'll need to put it back where we found it afterwards.
         */
        int headFirst = first.removeFirst();
        prefix.addLast(headFirst);
        weaveLists(first, second, results, prefix);
        prefix.removeLast();
        first.addFirst(headFirst);

        /** Do the same thing with seconf, damaging and then restoing the list. */
        int headSecond = second.removeFirst();
        prefix.addLast(headSecond);
        weaveLists(first, second, results, prefix);
        prefix.removeLast();
        second.addFirst(headSecond);
    }


}
