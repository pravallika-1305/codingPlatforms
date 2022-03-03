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

public List<Integer> postorderIterative(Node root){
  List<Integer> postorder = new ArrayList<Integer>();
  if(root == null) return postorder;
  Stack<Node> st1 = new Stack<Node>();
  Stack<Node> st2 = new Stack<Node>();
  st1.push(root);
  while(!st1.isEmpty()){
    root = st1.pop();
    st2.add(root);
    if (root.left != null) st1.push(root.left);
    if (root.right != null) st1.push(root.right);
   }
    while(!st2.isEmpty()){
      postorder.add(st2.pop().value);
   }
  return postorder;
}
