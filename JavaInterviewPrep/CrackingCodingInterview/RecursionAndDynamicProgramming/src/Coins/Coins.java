package Coins;

import java.util.ArrayList;

public class Coins {

    public static void main(String[] args) {
        int[] denoms = { 25, 10, 5, 1 };
        System.out.println("Ways: " + makeChange(10, denoms));
    }

    public static int makeChange(int amount, int[] denoms) {
        return makeChange(amount, denoms, 0);
    }

    public static int makeChange(int amount, int[] denoms, int index) {
        if(index >= denoms.length - 1) {
            return 1;
        }
        int ways = 0;
        for(int i = 0; i * denoms[index] <= amount; i++) {
            ways += makeChange(amount - (i * denoms[index]), denoms, index + 1);
        }
        return ways;
    }

    public static int makeChangeMemo(int amount, int[] denoms) {
        int[][] map = new int[amount + 1][denoms.length];
        return makeChangeMemo(amount, denoms, 0, map);
    }

    public static int makeChangeMemo(int amount, int[] denoms, int index, int[][] map) {
        if(map[amount][index] > 0) {
            return map[amount][index];
        }
        if(index >= denoms.length - 1) {
            return 1;
        }
        int ways = 0;
        for(int i = 0; i * denoms[index] <= amount; i++) {
            ways += makeChangeMemo(amount - (i * denoms[index]), denoms, index + 1, map);
        }
        map[amount][index] = ways;
        return ways;
    }


}
