import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] time = br.readLine().split(" ");

        int h = Integer.parseInt(time[0]);
        int m = Integer.parseInt(time[1]);
        if (m < 45) {
            if (h == 0) {
                h = 23;
                m += 15;
                System.out.println(h + " " + m);
                return ;
            }
            h--;
            m += 15;
            System.out.println(h + " " + m);
            return ;
        }
        m -= 45;

        System.out.println(h + " " + m);
    }
}
