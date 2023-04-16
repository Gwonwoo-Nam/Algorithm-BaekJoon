import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());

        if((N%4==0 && N%100!=0) || N%400==0) {
            System.out.println(1);
            return;
        }
        System.out.println(0);

    }

}
