import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int n = Integer.parseInt(input);

        int sum = 0;
        input= br.readLine();
        for (int i=0;i<n;i++) {
            sum += (input.charAt(i) - '0');
        }
        System.out.println(sum);

    }
}
