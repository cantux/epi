package Graph;

public abstract class AdjacencyArrayMatrix {
    int size;
    boolean[][] matrix;

    public AdjacencyArrayMatrix() {
        matrix = new boolean[1][1];
    }

    public void addNode() {
        boolean[][] newMatrix = new boolean[size+1][size+1];
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                newMatrix[i][j] = matrix[i][j];
            }
        }

        size++;
        matrix = newMatrix;
    }

    abstract public void addConnection(int from, int to);

}
