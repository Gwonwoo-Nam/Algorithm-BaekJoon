import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);
        inputs = br.readLine().split(" ");
        int[] cards = Arrays.stream(inputs).mapToInt(Integer::parseInt).toArray();

        int maxNum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    int sum = cards[i] + cards[j] + cards[k];
                    if (sum == m) {
                        maxNum = sum;
                        break;
                    }
                    if (sum < m && sum > maxNum) {
                        maxNum = sum;
                    }
                }
            }
        }
        System.out.println(maxNum);
    }
}
