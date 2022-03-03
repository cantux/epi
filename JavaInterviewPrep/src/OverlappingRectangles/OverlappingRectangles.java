package OverlappingRectangles;

class Rectangle {
    public Point bottomLeft;
    public Point topRight;
    public Rectangle(Point bl, Point tr) {
        bottomLeft = bl;
        topRight = tr;
    }

    public String toString() {
        return "bottomLeft: " + bottomLeft + " topRight: " + topRight;
    }
}

class Point {
    public int x, y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "x: " + x + " y: " + y;
    }
}

public class OverlappingRectangles {

    public static void main(String[] args) {
        Point p11 = new Point(1,1);
        Point p33 = new Point(3,3);

        Point p22 = new Point(2,2);
        Point p44 = new Point(4,4);
        Rectangle rec13 = new Rectangle(p11, p33);
        Rectangle rec24 = new Rectangle(p22, p44);

        System.out.println("result1: " + areaIntersecting(rec13, rec24));

        Point p01 = new Point(0,1);
        Point p10 = new Point(1, 0);

        Rectangle rec1022 = new Rectangle(p10, p22);
        Rectangle rec0133 = new Rectangle(p01, p33);

        System.out.println("result2: " + areaIntersecting(rec1022, rec0133));

        Point p00 = new Point(0,0);
        Rectangle rec0044 = new Rectangle(p00, p44);
        Rectangle rec1133 = new Rectangle(p11, p33);

        System.out.println("result3: " + areaIntersecting(rec0044, rec1133));
    }

    public static double areaIntersecting(Rectangle r1, Rectangle r2) {
        if(squaresIntersecting(r1, r2)) {

            return calculateArea(findIntersectingRec(r1, r2));
        }
        return 0.0;
    }

    public static Rectangle findIntersectingRec(Rectangle r1, Rectangle r2) {
        Rectangle retRect = new Rectangle(new Point(0, 0), new Point(0 ,0));
        if(r1.topRight.x < r2.topRight.x) {
            retRect.topRight.x = r1.topRight.x;
        }
        else {
            retRect.topRight.x = r2.topRight.x;
        }

        if(r1.topRight.y < r2.topRight.y) {
            retRect.topRight.y = r1.topRight.y;
        }
        else {
            retRect.topRight.y = r2.topRight.y;
        }

        if(r1.bottomLeft.x > r2.bottomLeft.x) {
            retRect.bottomLeft.x = r1.bottomLeft.x;
        }
        else {
            retRect.bottomLeft.x = r2.bottomLeft.x;
        }

        if(r1.bottomLeft.y > r2.bottomLeft.y) {
            retRect.bottomLeft.y = r1.bottomLeft.y;
        }
        else {
            retRect.bottomLeft.y = r2.bottomLeft.y;
        }

        System.out.println(retRect);
        return retRect;
    }

    public static double calculateArea(Rectangle rec) {
        return Math.abs(rec.bottomLeft.x - rec.topRight.x) * Math.abs(rec.bottomLeft.y - rec.topRight.y);
    }

    public static boolean squaresIntersecting(Rectangle r1, Rectangle r2) {
        return true;
    }
}
