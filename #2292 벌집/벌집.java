import static java.lang.Integer.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = parseInt(input);
        int sum = 1;
        int count = 1;
        while (n > sum) {
            sum += 6*count;
            count++;
        }
        System.out.println(count);
    }
}
