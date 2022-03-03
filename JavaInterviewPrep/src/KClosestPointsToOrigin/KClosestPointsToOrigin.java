//package KClosestPointsToOrigin;
//
//import java.util.Arrays;
//import java.util.Comparator;
//import java.util.List;
//import java.util.PriorityQueue;
//
//public class KClosestPointsToOrigin {
//    public static void main(String[] args) {
//        int[][] tuples = new int[][] {
//                {-2, 4},
//                {0, -2},
//                {-1, 0},
//                {3, 5},
//                {-2, -3},
//                {3, 2}
//        };
//        for(int[] a: kClosest(tuples)) {
//            System.out.println("result : " + Arrays.toString(a)) ;
//        }
//    }
//
//    static List<Integer[]> kClosest(int[][] tuples) {
//        for(int[] point: tuples) {
//            Math.sqrt(Math.pow(Math.abs(point[0]), 2) + Math.pow(Math.abs(point[1]), 2));
//        }
//
//        PriorityQueue<Integer[]> q = new PriorityQueue<>(new Comparator<Integer[]>() {
//            @Override
//            public int compare(Integer[] o1, Integer[] o2) {
//                return ;
//            }
//        });
//    }
//
//}
