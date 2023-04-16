import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int j = 0;j<t;j++) {
            String input = br.readLine();
            int sum = 0;
            int score = 0;
            for (int i = 0 ; i<input.length();i++) {
                if (input.charAt(i) == 'O') {
                    score++;
                    sum+=score;
                }
                if (input.charAt(i) == 'X') {
                    score = 0;
                }
            }
            System.out.println(sum);
        }



    }

}
