import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        Map<Character, Integer> alpha = new HashMap<>();
        for (int i = 0; i<input.length(); i++) {
            putSameChar(input, alpha, i);
            putDiffChar(input, alpha, i);

        }
        int max = 0;
        for (int value : alpha.values()) {
             if (value > max) {
                 max = value;
             }
        }
        int counter = 0;
        char result='\0';
        for (Map.Entry<Character, Integer> entry : alpha.entrySet()) {
            if (entry.getValue() == max) {
                result = entry.getKey();
                counter++;
            }
        }

        if (counter > 1) {
            System.out.println("?");
            return ;
        }
        System.out.println(result);
    }

    private static char toUpperCase(char alphabet) {
        if (alphabet >= 'a' && alphabet <= 'z') {
            alphabet = (char)(alphabet - 32);
        }
        return alphabet;
    }

    private static void putDiffChar(String input, Map<Character, Integer> alpha, int i) {
        char upperChar = toUpperCase(input.charAt(i));
        if (!alpha.containsKey(upperChar)) {
            alpha.put(upperChar, 1);
        }
    }

    private static void putSameChar(String input, Map<Character, Integer> alpha, int i) {
        char upperChar = toUpperCase(input.charAt(i));
        if (alpha.containsKey(upperChar)) {
            int value = alpha.get(upperChar) + 1;
            alpha.put(upperChar, value);
        }
    }
}