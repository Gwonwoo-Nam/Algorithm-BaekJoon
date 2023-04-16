
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        input = input.trim();

        if(input.equals("")) {
            System.out.println(0);
            return ;
        }
        System.out.println(input.split(" ").length);
    }
}

