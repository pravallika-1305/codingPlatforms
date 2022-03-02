/* Two types of Traversals:
  1. DFS
  2. BFS
 3 types of DFS:
  1. Preorder
  2. Inorder
  3. Postorder */

public void preorder(node) {
  /* Root, Left, Right*/
  
  if(node == null){
    return;
  }
  print(node.data);
  preorder(node.left);
  preorder(node.right);
}


public void inorder(node) {
  /*Left, Root, Right*/
  
  if(node == null){
    return;
  }
  inorder(node.left);
  print(node.data);
  inorder(node.right);
}
public void postorder(node) {
  /* Left, Right, Root*/
  
  if(node == null){
    return;
  }

  postorder(node.left);
  postorder(node.right);
  print(node.data);
}



  
  
