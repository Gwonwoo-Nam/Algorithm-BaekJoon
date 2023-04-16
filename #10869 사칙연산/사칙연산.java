import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String a = input.split(" ")[0];
        String b = input.split(" ")[1];

        int numA = Integer.parseInt(a);
        int numB = Integer.parseInt(b);
        System.out.println(numA+numB);
        System.out.println(numA-numB);
        System.out.println(numA*numB);
        System.out.println(numA/numB);
        System.out.println(numA%numB);


    }
}
