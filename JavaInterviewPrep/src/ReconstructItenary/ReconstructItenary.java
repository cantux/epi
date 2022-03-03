package ReconstructItenary;

import java.util.*;

public class ReconstructItenary {


    Map<String, PriorityQueue<String>> flights;

    public ReconstructItenary() {
        flights = new HashMap();
    }
    public List<String> findItinerary(String[][] tickets) {
        for (String[] ticket : tickets) {
            flights.putIfAbsent(ticket[0], new PriorityQueue<>());
            flights.get(ticket[0]).add(ticket[1]);
        }

        LinkedList<String> itinerary = new LinkedList();
        dfs("JFK", itinerary);
        return itinerary;
    }

    public void dfs(String departure, LinkedList path) {
        PriorityQueue<String> arrivals = flights.get(departure);
        while (arrivals != null && !arrivals.isEmpty())
            dfs(arrivals.poll(), path);
        path.addFirst(departure);
    }
}

class Test {
    public static void main(String[] args) {
        ReconstructItenary ri = new ReconstructItenary();
        String[][] test1 = new String[][]{{"MUC", "LHR"}, {"JFK", "MUC"}, {"SFO", "SJC"}, {"LHR", "SFO"}};
        String[][] test2 = new String[][]{{"JFK","SFO"},{"JFK","ATL"},{"SFO","ATL"},{"ATL","JFK"},{"ATL","SFO"}};
        System.out.println("Test 1 result: " + ri.findItinerary(test1));

        System.out.println("Test 2 result: " + ri.findItinerary(test2));
    }
}