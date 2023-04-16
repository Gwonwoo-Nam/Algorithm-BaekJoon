import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());
        StringBuffer result = new StringBuffer();
        String multi = Integer.toString(a*b*c);
        for (int i=0;i<10;i++) {
            int count = 0;
            for (int j=0;j<multi.length();j++) {
                if (multi.charAt(j) == i + '0') {
                    count++;
                }
            }
            result.append(count + "\n");
        }

        System.out.print(result);

    }
}