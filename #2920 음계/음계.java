import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");
        int[] numbers = Arrays.stream(inputs).mapToInt(Integer::parseInt).toArray();

        boolean ascendingCounter = true;
        boolean descendingCounter = true;
        for (int i = 0; i < 7; i++) {
            if (numbers[i] + 1 != numbers[i + 1] || numbers[0] != 1) {
                ascendingCounter = false;
            }
            if (numbers[i] - 1 != numbers[i + 1] || numbers[0] != 8) {
                descendingCounter = false;
            }
        }
        if (ascendingCounter) {
            System.out.println("ascending");
            return;
        }
        if (descendingCounter) {
            System.out.println("descending");
            return;
        }
        System.out.println("mixed");

    }

}
