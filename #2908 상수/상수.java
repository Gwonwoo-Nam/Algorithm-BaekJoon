import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");
        StringBuilder aStr = new StringBuilder(inputs[0]);
        int a = Integer.parseInt(aStr.reverse().toString());
        StringBuilder bStr = new StringBuilder(inputs[1]);
        int b = Integer.parseInt(bStr.reverse().toString());

        System.out.println(a > b ? a : b);

    }

}
