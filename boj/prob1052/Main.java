package prob1052;

import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        long n = Integer.parseInt(input.split(" ")[0]);
        long k = Integer.parseInt(input.split(" ")[1]);
        long totalN = n;

        int i = 0;
        long minNum = 0;
        //1~N-1 물병이 최대 2의 배수를 가지도록 탐색
        for (int j=0;j<k-1;j++) {
            while ((long)Math.pow(2,i) < n) {
                i++;
            }
            n = n - (long)Math.pow(2,i) / 2;
            minNum += (long)Math.pow(2,i) / 2;
            i = 0;
        }
        //마지막 물병은 Sum이 K보다 커지도록 최대 2의 배수를 탐색
        while ((long)Math.pow(2,i) < n) {
            i++;
        }
        minNum += (long)Math.pow(2,i);

        System.out.println(minNum - totalN);
    }
}
