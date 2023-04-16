
import java.util.Scanner;

public class Main {
    private enum Resistance{
        BLACK("black",0,1),
        BROWN("brown",1,10),
        RED("red",2,100),
        ORANGE("orange",3,1000),
        YELLOW("yellow",4,10000),
        GREEN("green",5,100000),
        BLUE("blue",6,1000000),
        VIOLET("violet",7,10000000),
        GREY("grey",8,100000000),
        WHITE("white",9,1000000000);
        private String name;
        private int value;
        private int multi;
        Resistance(String name, int value, int multi) {
            this.name = name;
            this.value = value;
            this.multi = multi;
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String first = scanner.nextLine();
        String second = scanner.nextLine();
        String third = scanner.nextLine();

        long result = 0;
        for (Resistance resistance : Resistance.values()) {
            if (first.equals(resistance.name)) {
                result += 10*resistance.value;
            }
            if (second.equals(resistance.name)) {
                result += resistance.value;
            }
        }
        for (Resistance resistance : Resistance.values()) {
            if (third.equals(resistance.name)) {
                result *= resistance.multi;
            }
        }
        System.out.println(result);
    }
}
