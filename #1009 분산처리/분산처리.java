import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        int caseNum = Integer.parseInt(input);


        for (int i=0; i<caseNum;i++) {
            String inputLine = scanner.nextLine();
            long a = Integer.parseInt(inputLine.split(" ")[0]);
            long b = Integer.parseInt(inputLine.split(" ")[1]);
            long result = 1;
            for (int j = 1; j <= b; j++) {
                result = (a * result) % 10;
            }
            if (result == 0) {
                result = 10;
            }
            System.out.println(result);
        }
    }
}