import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while ((input=br.readLine())!=null && !input.isEmpty()) {
            String[] inputs = input.split(" ");
            if (inputs.length == 1) {
                continue;
            }
            int r = Integer.parseInt(inputs[0]);
            String s =  inputs[1];
            StringBuffer result = new StringBuffer();
            for (int i=0; i<s.length();i++) {
                for (int j = 0; j<r;j++) {
                    result.append(s.charAt(i));
                }
            }
            System.out.println(result);
        }
    }
}
