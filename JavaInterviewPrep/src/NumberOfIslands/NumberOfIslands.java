package NumberOfIslands;

import javafx.util.Pair;

import java.util.ArrayList;
import java.util.List;

public class NumberOfIslands {
    public static void main(String[] args) {
        int[][] islands = new int[][]{
                {1, 1, 1, 1, 0},
                {1, 1, 0, 1, 0},
                {1, 1, 0, 0, 0},
                {0, 0, 0, 0, 0}
        };
        System.out.println("result: " + findNo(islands));

        int[][] islands2 = new int[][]{
                { 1, 1, 0, 0, 0 },
                { 1, 1, 0, 0, 0 },
                { 0, 0, 1, 0, 0 },
                { 0, 0, 0, 1, 1 }
        };
        System.out.println("result: " + findNo(islands2));
    }

    public static int findNo(int[][] islands) {
        int rowLength = islands.length;
        int colLength;
        if(rowLength == 0) {
            return 0;
        }
        else {
            colLength = islands[0].length;
        }

        int islandCount = 0;
        // start traversing the array,
        // when encountered a node with a value of 1
        // increment the island count by one and start a dfs from that node,
        // dfs should set all the neighbors to 0

        for(int r = 0; r < rowLength; r++) {
            for(int c = 0; c < colLength; c++) {
                if(islands[r][c] == 1) {
                    dfs(islands, r, c);
                    islandCount++;
                }
            }
        }
        return islandCount;
    }

    public static void dfs(int[][] islands, int row, int col) {
        islands[row][col] = 0;
        List<Pair<Integer, Integer>> neighborList = getNeighbors(islands, row, col);
        if(neighborList.isEmpty()) {
            return;
        }
        for(Pair<Integer, Integer> rowColPair: neighborList) {
            dfs(islands, rowColPair.getKey(), rowColPair.getValue());
        }
    }

    public static List<Pair<Integer, Integer>> getNeighbors(int[][] islands, int row, int col) {
        List<Pair<Integer, Integer>> neighborList = new ArrayList<>();
        for(int i = -1; i <= 1; i++) {
            for(int j = -1; j <= 1; j++) {
                if(i == j) continue;
                if(row + i < islands.length
                        && col + j < islands[0].length
                        && row + i >= 0
                        && col + j >= 0
                        && islands[row + i][col + j] == 1) {
                    neighborList.add(new Pair(row + i, col + j));
                }
            }
        }
        return neighborList;
    }
}
