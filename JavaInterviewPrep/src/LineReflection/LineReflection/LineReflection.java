package LineReflection.LineReflection;

import java.util.*;

public class LineReflection {
    public static void main(String[] args) {

        int[][] arr1 = new int[][] {
                {3, 1},
                {-1, 1},
                {-2, 1},
                {2, 1},
        };

        System.out.println("true: " + isReflected(arr1));

        int[][] arr13 = new int[][] {
                {3, 1},
                {-1, 1},
                {-2, 1},
                {1, 1},
        };

        System.out.println("false: " + isReflected(arr13));

        int[][] arr11 = new int[][] {
                {3, 1},
                {-1, 1},
                {-2, 1}
        };

        System.out.println("false: " + isReflected(arr11));

        int[][] arr12 = new int[][] {
                {3, 1},
                {-1, 1}
        };

        System.out.println("true: " + isReflected(arr12));


        int[][] arr = new int[][] {
                {1, 1},
                {-2, 1}
        };

        System.out.println("true: " + isReflected(arr));

        int[][] arr2 = new int[][] {
                {1, 1},
                {-1, 1},
                {-2, 1},
                {2, 1},
                {1, 2},
                {-1, 2},
                {-2, 2},
                {2, 2},
                {-2, 3},
                {2, 3},
        };

        System.out.println("true: " + isReflected(arr2));
    }


    public static boolean isReflected(int[][] points) {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        HashSet<String> set = new HashSet<>();
        for(int[] p:points){
            max = Math.max(max,p[0]);
            min = Math.min(min,p[0]);
            String str = p[0] + "a" + p[1];
            set.add(str);
        }
        int sum = max+min;
        for(int[] p:points){
            //int[] arr = {sum-p[0],p[1]};
            String str = (sum-p[0]) + "a" + p[1];
            if( !set.contains(str))
                return false;

        }
        return true;
    }

//    public static boolean isReflected(int[][] points) {
//        // find a line that makes the points reflect each other means that, it should be in equal distance.
//        // the condition parallel to  means that given (x1, y1), (x2, y2) their y's must be equal.
//
//        // so it's enough to group together the points by their y
//        // LinkedHashTable might help us acheive that.
//
//        // First of all though, sort the array by x so that down the line we don't have to do it over again for every y1 = yn
//        if(points.length == 0) return false;
//        Arrays.sort(points, new Comparator<int[]>() {
//            @Override
//            public int compare(int[] o1, int[] o2) {
//                return o1[0] - o2[0];
//            }
//        });
//
//        // <point y, nodeIndex>
//        Map<Integer, List<Integer>> mapOfYsToNodeIndeces = new HashMap();
//
//        for(int i = 0; i < points.length; i++) {
//            int y = points[i][1];
//            if(mapOfYsToNodeIndeces.containsKey(y)) {
//                List<Integer> indecesList = mapOfYsToNodeIndeces.get(y);
//                indecesList.add(i);
//                mapOfYsToNodeIndeces.put(y, indecesList);
//            }
//            else {
//                List<Integer> indecesList = new ArrayList();
//                indecesList.add(i);
//                mapOfYsToNodeIndeces.put(points[i][1], indecesList);
//            }
//        }
//
//        Iterator<Map.Entry<Integer, List<Integer>>> it = mapOfYsToNodeIndeces.entrySet().iterator();
//
//        Map.Entry<Integer, List<Integer>> firstEntry = it.next();
//        List<Integer> indecesList = firstEntry.getValue();
//
//        Double positionX = null;
//        if(!helper(indecesList, points, positionX)) {
//            return false;
//        }
//
//        while(it.hasNext()) {
//            Double newPositionX = null;
//            if(!helper(it.next().getValue(), points, newPositionX))  {
//                return false;
//            }
//            if(positionX != newPositionX){
//                return false;
//            }
//        }
//
//        return true;
//    }


    public static boolean helper(List<Integer> indecesList, int[][] points, Double positionX) {
        // given 4 x points partition them in such a way the there is a middle.
        // 2 4 6 8 has middle 5.. 1 2 4 6 has no middle. I should think about this a little while on paper
        // sort then check it from the middle
        if(indecesList.size() % 2 != 0) {
            return false;
        }
        else {
            int middle = indecesList.size() / 2;
            int middleX = points[indecesList.get(middle - 1)][0];
            double lengthBetweenTwoMiddlePoints = Math.abs(middleX  - points[indecesList.get(middle)][0]);
            positionX = middleX + (lengthBetweenTwoMiddlePoints / 2);

//            System.out.println("positionX: " + positionX);
//            System.out.println("lengthBetweenTwoMiddlePoints: " + lengthBetweenTwoMiddlePoints);

            double newPositionX;
            for(int i = 1; i < middle; i++) {
                int newMiddleX = points[indecesList.get(middle -1 - i)][0];

                double newLengthBetweenTwoMiddlePoints = Math.abs(newMiddleX  - points[indecesList.get(middle + i)][0]);
//                System.out.println("newLengthBetweenTwoMiddlePoints: " + newLengthBetweenTwoMiddlePoints);

                newPositionX = newMiddleX + (newLengthBetweenTwoMiddlePoints / 2);
//                System.out.println("new pos x: " + newPositionX);

                if(newPositionX != positionX) {
                    return false;
                }
            }
        }
        return true;
    }
}
