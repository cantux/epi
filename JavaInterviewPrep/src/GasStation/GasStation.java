package GasStation;

/**
 * There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
 *
 * You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
 *
 * Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
 */


public class GasStation {
// go along the for loop to find the extra gas required by every station.
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int tank=0, total=0, start=0;
        for(int i=0; i<gas.length; i++) {
            int current = gas[i]-cost[i];
            tank += current;
            total += current;
            if(tank < 0) {
                start = i+1;
                tank = 0;
            }
        }

        if (start == gas.length) return -1;
        return total < 0 ? -1 : start;
    }
}
