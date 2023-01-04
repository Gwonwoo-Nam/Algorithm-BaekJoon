package prob1000;


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        int answer = 0;
        for (String each : input.split(" ")) {
            answer += Integer.parseInt(each);
        }
        System.out.println(answer);
    }
}


