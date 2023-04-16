import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();

        for (char i = 'a'; i <= 'z'; i++) {
            int loc = -1;
            for (int j = 0; j < word.length(); j++) {
                if (i==word.charAt(j)) {
                    loc = j;
                    break ;
                }
            }
            System.out.print(loc);
            if (!(i == 'z'))
                System.out.print(" ");
        }
    }
}
