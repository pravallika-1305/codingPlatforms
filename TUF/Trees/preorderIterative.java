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

public List<Integer> preorderIterative(Node root){
  List<Integer> preorder = new ArrayList<Integer>();
  if(root == null) return preorder;
  Stack<Node> st = new Stack<Node>();
  st.push(root);
  while(!st.isEmpty()){
    root = st.pop();
    preorder.add(root.value);
    if (root.right != null) st.push(root.right);
    if (root.left != null) st.push(root.left);
   }
  return preorder;
}
