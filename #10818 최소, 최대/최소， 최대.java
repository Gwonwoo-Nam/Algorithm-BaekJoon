import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = Integer.parseInt(input);
        int[] numbers = new int[n];

        String numberLine = br.readLine();
        String[] numberStrings = numberLine.split(" ");


        int min = Integer.parseInt(numberStrings[0]);
        int max = Integer.parseInt(numberStrings[0]);
        for (int count=0;count<n; count++) {
            numbers[count] = Integer.parseInt(numberStrings[count]);
            if (numbers[count] > max) {
                max = numbers[count];
            }
            if (numbers[count] < min) {
                min = numbers[count];
            }
        }
        System.out.println(min + " " + max);
    }
}

