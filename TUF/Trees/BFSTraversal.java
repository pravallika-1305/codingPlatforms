public class Node{
  int value;
  Node left;
  Node right;
  public Node(){}
  public Node(int key){
    this.value = key;
  }
  public Node(int key, Node leftVal, Node rightVal){
    this.value = key;
    this.left = leftVal;
    this.right = rightVal;
  }
}

public List<List<Integer>> BFSTraversal(Node root){
  Queue<Node> queue = new LinkedList<Node>();
  List<List<Integer>> wrapList = new LinkedList<List<Integer>>();
  if(root === null) return wrapList;
  queue.offer(root);
  while(!queue.isEmpty()){
    int nodesInTheLevel = queue.size();
    List<Integer> levelList = new LinkedList<Integer>();
    for(int i = 0; i < nodesInTheLevel; i++){
      if (queue.peek().left != null) queue.offer(queue.peek().left);
      if (queue.peek().right != null) queue.offer(queue.peek().right);
      levelList.add(queue.poll().value);
    }
      wrapList.add(levelList);
   }
  return wrapList;
}
    
      
    
