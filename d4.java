import java.util.Scanner;

public class d4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter color code: ");
        int color = scanner.nextInt();
        
        switch (color) {
            case 1:
                System.out.println("The next traffic light is green");
                break;
            case 2:
                System.out.println("The next traffic light is orange");
                break;
            case 3:
                System.out.println("The next traffic light is red");
                break;
            default:
                System.out.println("Out of range...");
                break;
        }
    }
}
