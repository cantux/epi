package PrintArrayZigZag;

public class PrintArrayZigZag {
    public static void main(String[] args) {
        int mat[][] = { {1, 2, 3, 4, 5},
                {6, 7, 8, 9, 10},
                {11, 12, 13, 14, 15}};
        printZigZag(mat);
    }

    static void printZigZag(int[][] arr) {
        int rowLength = arr.length;
        int colLength = arr[0].length;
        for(int r = 0; r < rowLength; r++) {
            if(r % 2 == 0) {
                for(int c = 0; c < colLength; c++) {
                    System.out.print(arr[r][c]);
                }
            }
            else {
                for(int c = colLength - 1; c >= 0; c--) {
                    System.out.print(arr[r][c]);
                }
            }
            System.out.println();
        }
    }
}
