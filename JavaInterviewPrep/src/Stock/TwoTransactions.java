package Stock;

import java.util.ArrayList;

public class TwoTransactions {
    public static void main(String[] args) {
        ArrayList<int[]> list = new ArrayList<>();
        list.add(new int[] {10, 15, 30 });
        list.add(new int[] {10, 20, 15, 30 });
        list.add(new int[] {15, 10, 30 });

        list.add(new int[] {30, 15, 10 });
        list.add(new int[] {30, 15, 20, 10 });
        list.add(new int[] {30, 10, 15 });

        list.add(new int[] {10, 15, 30, 5 });
        list.add(new int[] {10, 20, 15, 30, 5 });
        list.add(new int[] {15, 10, 30, 5 });

        list.add(new int[] {30, 15, 10, 5 });
        list.add(new int[] {30, 15, 20, 10, 5 });
        list.add(new int[] {30, 10, 15, 5});

        for(int[] i : list) {
            System.out.println("loss result: " + maxLoss(i));
        }

        for(int[] i : list) {
            System.out.println("profit result: " + maxProfit(i));
        }
    }

    public static int maxLoss(int[] dailyStockValue) {
        int max = Integer.MIN_VALUE;
        int maxLoss = Integer.MIN_VALUE;
        for(int i = 0; i < dailyStockValue.length; i++) {
            max = Math.max(max, dailyStockValue[i]);
            maxLoss = Math.max(maxLoss, max - dailyStockValue[i]);
        }

        return maxLoss;
    }

    public static int maxProfit(int[] dailyStockValue) {
        int min = Integer.MAX_VALUE;
        int maxProfit = Integer.MIN_VALUE;
        for(int i = 0; i < dailyStockValue.length; i++) {
            min = Math.min(min, dailyStockValue[i]);
            maxProfit = Math.max(maxProfit, dailyStockValue[i] - min);
        }

        return maxProfit;
    }
}
