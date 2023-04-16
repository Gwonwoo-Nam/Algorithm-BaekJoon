
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        int max=0;
        int maxIndex =0;
        int[] numbers = new int[9];
        for (int i=0;i<9;i++) {
            input = br.readLine();
            numbers[i]=Integer.parseInt(input);
            if (numbers[i] > max) {
                max = numbers[i];
                maxIndex = i+1;
            }
        }

        System.out.println(max);
        System.out.println(maxIndex);


    }
}