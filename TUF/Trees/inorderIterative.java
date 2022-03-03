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

public List<Integer> inorderIterative(Node root){
  List<Integer> inorder = new ArrayList<Integer>();
  if(root == null) return inorder;
  // use stack data structure instead of auxiliary stack space of recursion 
  Stack<Node> st = new Stack<Node>(); //LIFO Data structure
  Node node = root;
  while(true){
    if(node != null){
      st.push(node);
      node = node.left;
    } else {
      if(st.isEmpty()) break;
      node = st.pop();
      inorder.add(node.value);
      node = node.right;
    }
   }
  return inorder;
}
