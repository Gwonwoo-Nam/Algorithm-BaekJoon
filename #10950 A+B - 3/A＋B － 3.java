import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int t = Integer.parseInt(input);
        for (int i=0;i<t;i++) {
            input = br.readLine();
            int a = Integer.parseInt(input.split(" ")[0]);
            int b = Integer.parseInt(input.split(" ")[1]);
            System.out.println(a+b);
        }

    }
}
