package WithinTriangle;

class Point {
    public int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class WithinTriangle {

    public static void main(String[] args) {
        System.out.println("result: " +
                isInside(
                new Point(0,4),
                new Point(0, 0),
                new Point(3, 0),
                new Point(1,1)
        ));
    }

    public static boolean isInside(Point p1, Point p2, Point p3, Point target) {
        return isInside(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y, target.x, target.y);
    }
    public static double pointDistance(Point p1, Point p2) {
        return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
    }

    public static double area(int x1, int y1, int x2, int y2,
                       int x3, int y3)
    {
        return Math.abs((x1*(y2-y3) + x2*(y3-y1)+
                x3*(y1-y2))/2.0);
    }

    /* A function to check whether point P(x, y) lies
       inside the triangle formed by A(x1, y1),
       B(x2, y2) and C(x3, y3) */
    public static boolean isInside(int x1, int y1, int x2,
                            int y2, int x3, int y3, int x, int y)
    {
        /* Calculate area of triangle ABC */
        double A = area (x1, y1, x2, y2, x3, y3);

        /* Calculate area of triangle PBC */
        double A1 = area (x, y, x2, y2, x3, y3);

        /* Calculate area of triangle PAC */
        double A2 = area (x1, y1, x, y, x3, y3);

        /* Calculate area of triangle PAB */
        double A3 = area (x1, y1, x2, y2, x, y);

        /* Check if sum of A1, A2 and A3 is same as A */
        return (A == A1 + A2 + A3);
    }
    public static boolean isOnTheEdge(Point p1, Point p2, Point p3, Point target) {
        double edge1 = pointDistance(p1, p2);
        double edge2 = pointDistance(p1, p3);
        double edge3 = pointDistance(p2, p3);

        // for checking against p1
        double distanceToP1 = pointDistance(p1, target);
        double distanceToP2 = pointDistance(p2, target);
        double distanceToP3 = pointDistance(p3, target);
        boolean within = edge1 < edge2 ? (edge1 < distanceToP1 && distanceToP1 < edge2) : (edge1 > distanceToP1 && distanceToP1 > edge2);
        within &= edge1 < edge3 ? (edge1 < distanceToP2 && distanceToP2 < edge3) : (edge1 > distanceToP2 && distanceToP2 > edge3);
        within &= edge2 < edge3 ? (edge2 < distanceToP3 && distanceToP3 < edge3) : (edge2 > distanceToP3 && distanceToP3 > edge3);

        return within;
    }
}
