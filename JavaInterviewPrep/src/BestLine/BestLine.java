package BestLine;

class GraphPoint {
    public int x ,y;
    public GraphPoint(int x, int y) {this.x = x; this.y = y;}
}

class Line {
    // epsilon used to lower the precision
    // cuz floating point operations doesnt always yield the same result
    public static double epsilon = .0001;

    public double slope, intercept; // intercept: where the line intercepts the y line.

    private boolean infinite_slope = false;

    public Line(GraphPoint p1, GraphPoint p2) {
        if(Math.abs(p1.x - p2.x) > epsilon) {
            slope = p1.y - p2.y / p1.x - p2.x;
            intercept = p1.y - slope * p1.x;
        }
        else {
            infinite_slope = true;
            intercept = p1.x; // switch intercept to x if line is infinite
        }
    }

    public static double floorToNearestEpsilon(double d) {
        int r = (int) (d / epsilon);
        return (double) (r * epsilon);
    }

    public boolean isEquivalent(double a, double b) {
        return Math.abs(a - b) < epsilon;
    }

    public boolean isEquivalent(Object o) {
        Line l = (Line) o;
        return isEquivalent(l.slope, slope)
                && isEquivalent(l.intercept, intercept)
                && infinite_slope == l.infinite_slope;
    }
}

public class BestLine {

    public static void main(String[] args) {
//        GraphPoint[] g = new GraphPoint[]
//                {
//                        new GraphPoint()
//                };
    }

//    public findBestLine()
}
