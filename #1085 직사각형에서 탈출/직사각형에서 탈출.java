import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int[] positions = Arrays.stream(inputs).mapToInt(Integer::parseInt).toArray();

        int x = Math.min(positions[2] - positions[0], positions[0]);
        int y = Math.min(positions[3]-positions[1],positions[1]);
        System.out.println(Math.min(x,y));
    }
}

