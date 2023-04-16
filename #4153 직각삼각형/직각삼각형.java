

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));



        while (true) {
            String[] inputs = br.readLine().split(" ");

            int[] numbers = Arrays.stream(inputs).mapToInt(Integer::parseInt).toArray();
            if (numbers[0] == 0 && numbers[1] == 0 && numbers[2] == 0 ) {
                return ;
            }
            if (condition(numbers[0],numbers[1],numbers[2])) {
                System.out.println("right");
                continue ;
            }
            System.out.println("wrong");

        }

    }

    public static int multi(int num) {
        return num*num;
    }

    public static boolean condition(int a, int b, int c) {
        if (multi(a) == multi(b) + multi(c)) {
            return true;
        }
        if (multi(b) == multi(a) + multi(c)) {
            return true;
        }
        if (multi(c) == multi(a) + multi(b)) {
            return true;
        }
        return false;
    }

}
