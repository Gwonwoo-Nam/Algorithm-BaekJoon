import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Node node = new Node(Integer.parseInt(br.readLine()));
        String token;

        while ((token = br.readLine()) != null) {
            if (token.equals("")) {
                break ;
            }
            node.insert(Integer.parseInt(token));
        }
        postOrder(node);


    }

    public static void postOrder(Node tree) {
        if (tree != null) {
            if (tree.left != null) {
                postOrder(tree.left);
            }
            if (tree.right != null) {
                postOrder(tree.right);
            }
            System.out.println(tree.value);
        }
    }
}

class Node {
    Node left;
    Node right;
    int value;
    public Node(int value) {
        this.value = value;
    }
    public Node(int value, Node left, Node right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
    void insert(int n) {
        if (n < this.value) {
            //왼칸이 비어있으면
            if (this.left == null) {
                this.left = new Node(n);
            }
            //하위 노드에서 탐색
            else this.left.insert(n);
        } else {
            //오른칸이 비어있으면
            if (this.right == null) {
                this.right = new Node(n);
            }
            else this.right.insert(n);
        }
    }

}
