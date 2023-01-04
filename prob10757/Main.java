package prob10757;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        StringBuffer a = new StringBuffer(input.split(" ")[0]);
        StringBuffer b = new StringBuffer(input.split(" ")[1]);
        StringBuffer result = new StringBuffer();

        int i = 0;
        int carry = 0;

        while (a.length() > b.length()) {
            b.insert(0,0);
        }
        while (a.length() < b.length()) {
            a.insert(0,0);
        }
        int size = a.length();

        while (size != i) { //a또는 b가 0번째 인덱스가 되면
            int total = (int)(a.charAt(a.length() - i - 1) - '0') + (int)(b.charAt(b.length() - i - 1) - '0') + carry;
            int sum = total % 10;
            carry = total / 10;
            result.insert(0, sum);
            i++;
        }
        if (carry != 0) {
            result.insert(0,carry);
        }

        System.out.println(result);
    }
}
