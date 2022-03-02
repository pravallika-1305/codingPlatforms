/* Two types of Traversals:
  1. DFS
  2. BFS
 3 types of DFS:
  1. Preorder
  2. Inorder
  3. Postorder */
public class Node{
  int data;
  Node left;
  Node right;
  
  public Node(key){
    this.data = key;
  }
}

public void preorder( Node node) {
  /* Root, Left, Right*/
  
  if(node == null){
    return;
  }
  print(node.data);
  preorder(node.left);
  preorder(node.right);
}


public void inorder(Node node) {
  /*Left, Root, Right*/
  
  if(node == null){
    return;
  }
  inorder(node.left);
  print(node.data);
  inorder(node.right);
}
public void postorder(Node node) {
  /* Left, Right, Root*/
  
  if(node == null){
    return;
  }

  postorder(node.left);
  postorder(node.right);
  print(node.data);
}



  
  
