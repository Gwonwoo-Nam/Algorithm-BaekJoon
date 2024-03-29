import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());
        int[] aArray = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = Integer.parseInt(br.readLine());
        int[] keys = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        //정렬
        Arrays.sort(aArray);

        for (int key : keys) {
            System.out.println(search(key, aArray));
        }
    }

    public static int search(int key, int[] aArray) {
        //return Arrays.binarySearch(aArray, key);
        int high = aArray.length;
        int low = 0;
        int mid;
        while (low + 1 < high) {
            mid = (high + low) / 2;
            if (aArray[mid] <= key) {
                low = mid;
            }
            else {
                high = mid;
            }
        }
        if (aArray[low] == key) {
            return 1;
        }
        return 0;
    }
}