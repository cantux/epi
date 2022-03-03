package KthMin.KthMin;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

public class KthMin {

    public static void main(String[] args) {
        ArrayList<int[]> list = new ArrayList<>();

        list.add(new int[]{1, 2, 3, 4, 5, 6});
        list.add(new int[]{3, 3, 4});
        list.add(new int[]{2, 3});
        list.add(new int[]{});

        for(int[] arr : list) {
            System.out.println("result: " + kthMin(arr, 4));
            System.out.println("qs part: " + kthMin(arr, 3));
            System.out.println("qs rand: " + kthMin(arr, 2));
        }
    }

    public static Integer kthMin(int[] arr, int k) {

        if(arr.length < k) {
            return -1;
        }

        Comparator<Integer> comp = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
            }
        };

        final PriorityQueue<Integer> pq = new PriorityQueue<>(k, comp);
        for(int val : arr) {
            pq.offer(val);

            if(pq.size() > k) {
                pq.poll();
            }
        }
        return pq.peek();
    }


}
