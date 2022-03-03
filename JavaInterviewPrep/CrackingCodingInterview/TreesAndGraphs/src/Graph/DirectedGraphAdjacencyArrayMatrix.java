package Graph;

public class DirectedGraphAdjacencyArrayMatrix extends AdjacencyArrayMatrix {
    @Override
    public void addConnection(int from, int to) {
        this.matrix[from][to] = true;
    }
}
