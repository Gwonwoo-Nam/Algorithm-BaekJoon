package prob1546;


import static java.lang.Integer.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = parseInt(input);

        input = br.readLine();
        String[] inputSplit = input.split(" ");
        int[] scores = Stream.of(inputSplit).mapToInt(Integer::parseInt).toArray();

        double max = Arrays.stream(scores).max().getAsInt();

        double[] average = Arrays.stream(scores).mapToDouble(x->(double)x/max*100).toArray();

        double sum = 0;
        for (int i =0;i<average.length;i++) {
            sum += average[i];
        }
        double result = sum/average.length;
        System.out.println(result);

    }
}
