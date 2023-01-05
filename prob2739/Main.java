package prob2739;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = Integer.parseInt(scanner.nextLine());

        for (int i = 1; i <= 9; i++) {
            System.out.println(input + " * " + i + " = " + input * i);
        }

    }

}
