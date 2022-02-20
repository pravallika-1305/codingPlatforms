// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
// X -> occupied
// . -> no obstacle

//objectifying the coordinates of the robot
class Node{
    int row;
    int col;
    public Node(int row, int col){
        this.row = row;
        this.col = col;
    }
    public int getRow(){
        return this.row;
    }
    public int getCol(){
        return this.col;
    }
    public boolean equals(Object obj){
        Node node = (Node) obj;
        if(node.getRow() == row && node.getCol() == col) {
        return true;
        } 
        return false;
        
    }
    public int hashCode(){
        return Objects.hashCode(this.row) * Objects.hashCode(this.col);
    }
}

class Solution {
    
    Set<Node> set = new HashSet<>();
    //left, right, up, down movements
    final int[] directions = new int[]{1,2,3,4};

    public int solve(char[][] board){
        Map<String, Boolean> visited = new HashMap<>();
        dfs(board, 0, 0, 0, visited);
        return set.size();

    }
    public void dfs(char[][] board, int row, int col, int direction, Map<String, Boolean> visited) {
        String key = row+":"+ col + ":" + direction;
        if(visited.containsKey(key)){
            return;
        }
        if(row == board.length || row == -1 || col == -1 || col == board[0].length){
            //go back to the previous coordinates and change direction
            if(row == board.length){
                dfs(board, row - 1, col, 2, visited);
            } else if (row == -1){
                dfs(board, row + 1, col, 0, visited);
            } else if (col == board[0].length){
                dfs(board, row, col - 1, 1, visited);
            } else if (col == -1){
                dfs(board, row, col + 1, 3, visited);
            }
            return;
        }
        visited.put(key, true);

        if(board[row][col] != 'X'){
            // move in the same direction
            Node node = new Node(row, col);
            set.add(node);
            if(direction == 0){
                dfs(board, row, col + 1, 0, visited);
            } else if(direction == 1){
                dfs(board, row + 1, col, 1, visited);
            } else if(direction == 2){
                dfs(board, row, col - 1, 2, visited);
            } else{
                dfs(board, row - 1, col, 3, visited);
            }
        } else {
            //go to previous coordinates and change direction
            if(direction == 0){
                dfs(board, row, col - 1, 1, visited);            
            } else if(direction == 1){
                dfs(board, row - 1, col, 2, visited);
            } else if(direction == 2){
                dfs(board, row, col + 1, 3, visited);
            } else {
                dfs(board, row + 1, col, 0, visited);
            }
        }
    }
    public int solution(String[] R) {
        // write your code in Java SE 8
        int rows = R.length;
        int columns = R[0].length();
        char[][] board = new char[rows][columns];
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < columns; j++){
                board[i][j] = R[i].charAt(j);
            }
        }
        return solve(board);
    }
}
