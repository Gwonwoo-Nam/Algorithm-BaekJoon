
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = Integer.parseInt(input.split(" ")[0]);
        int x = Integer.parseInt(input.split(" ")[1]);
        int numbers[] = new int[n];
        input = br.readLine();
        for (int i= 0; i<n;i++) {
            numbers[i] = Integer.parseInt(input.split(" ")[i]);
        }
        StringBuffer output = new StringBuffer("");
        for (int i= 0; i<n;i++) {
            if (numbers[i] < x) {
                output.append(numbers[i]);
                output.append(" ");
            }
        }
        System.out.print(output.toString().trim());

    }
}
