package RobotInAGrid;

import javafx.util.Pair;

import java.util.ArrayList;

/**
 * Imagine a robot sitting on the upper left corner of a grid with r rows and c columns.
 * The robot can only move in two directions, right and down, bur certain cells are off limits such that the robot cannot step on them.
 * Design an algorithm to find a path for the robot from the top of the left bottom right.
 */
public class RobotInAGrid {
    public static void main(String[] args) {
        boolean[][] maze0 = {
                {true,  true,  true,  false, false},
                {true,  true,  true,  true,  false},
                {true,  true,  false, true,  true },
                {false, true,  true,  true,  true },
                {false, false, true,  true,  true },
        };

        boolean[][] maze1 = {
                {true,  true,  true,  false, false},
                {true,  true,  true,  true,  false},
                {true,  true,  true,  false, false},
                {false, false, true,  true,  true },
                {false, false, true,  true,  true },
        };

        System.out.println("Solution to maze0 is: " + findPath(maze0));
        System.out.println("Solution to maze1 is: " + findPath(maze1));
    }

    public static ArrayList<Pair<Integer, Integer>> findPath(boolean[][] maze) {
        ArrayList<Pair<Integer, Integer>> list = new ArrayList();
        getPath(maze, maze.length - 1, maze[0].length - 1, list);
        return list;
    }

    public static boolean getPath(boolean[][] maze, int row, int col, ArrayList<Pair<Integer, Integer>> list) {
        if(row < 0 || col < 0 || !maze[row][col]) {
            return false;
        }

        boolean isAtOrigin = ((row == 0) && (col == 0));

        if(isAtOrigin || getPath(maze, row - 1, col, list) || getPath(maze, row, col - 1, list)) {
            list.add(new Pair(row, col));
            return true;
        }
        return false;
    }
}
