

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i=0;i<t;i++) {
            String[] input = br.readLine().split(" ");
            int h = Integer.parseInt(input[0]);
            int w = Integer.parseInt(input[1]);
            int n = Integer.parseInt(input[2]);
            int floor = (n%h==0) ? h : n % h;
            int loc = (n%h==0) ? n/h : n / h + 1;

            StringBuffer sb = new StringBuffer();
            sb.append(floor);
            if (loc/10 == 0) {
                sb.append("0");
            }
            sb.append(loc);

            System.out.println(sb);
        }


    }

}
