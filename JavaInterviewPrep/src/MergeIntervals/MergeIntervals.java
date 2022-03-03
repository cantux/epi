package MergeIntervals;

import java.util.*;

class Interval {
    int start;
    int end;
    Interval() { start = 0; end = 0; }
    Interval(int s, int e) { start = s; end = e; }
}

public class MergeIntervals {
    public List<Interval> merge3(List<Interval> intervals) {
        List<Interval> ret = new ArrayList<>();
        int n = intervals.size();
        if(n == 1) return intervals;
        if(n == 0) return ret;

        PriorityQueue<Interval> pq = new PriorityQueue<Interval>((a, b) -> (a.start - b.start));

        for(Interval z: intervals) {
            pq.offer(z);
        }

        Interval current = pq.poll();
        while(!pq.isEmpty()) {
            Interval next = pq.poll();
            if(current.end >= next.start) {
                current.end = Math.max(next.end, current.end);
            }
            else {
                ret.add(current);
                current = next;
            }
        }
        ret.add(current);
        return ret;
    }

    public static List<Interval> merge(List<Interval> intervals) {
        Collections.sort(intervals, new Comparator<Interval>() {
            public int compare(Interval i1, Interval i2) {
                return i1.start - i2.start;
            }
        });


        LinkedList<Interval> merged = new LinkedList<Interval>();
        for (Interval interval : intervals) {
            // if the list of merged intervals is empty or if the current
            // interval does not overlap with the previous, simply append it.
            if (merged.isEmpty() || merged.getLast().end < interval.start) {
                merged.add(interval);
            }
            // otherwise, there is overlap, so we merge the current and previous
            // intervals.
            else {
                merged.getLast().end = Math.max(merged.getLast().end, interval.end);
            }
        }

        return merged;
    }

    public static List<Interval> merge2(List<Interval> intervals) {
        // sort start&end
        int n = intervals.size();
        int[] starts = new int[n];
        int[] ends = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = intervals.get(i).start;
            ends[i] = intervals.get(i).end;
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        // loop through
        List<Interval> res = new ArrayList<Interval>();
        for (int i = 0, j = 0; i < n; i++) { // j is start of interval.
            if (i == n - 1 || starts[i + 1] > ends[i]) {
                res.add(new Interval(starts[j], ends[i]));
                j = i + 1;
            }
        }
        return res;
    }
}
