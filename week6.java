import java.util.Scanner;
public class week6{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("enter color code: ");
        int color = scanner.nextInt();
        //== comparison True, flase
        if (color == 1){
        System.out.println("the  next traffic light is green ");
        }else if (color == 2){
            System.out.println("the next traffic light is orange ");
        }else if (color  == 3){
            System.out.println(" the next traffic light is red  ");
        }else{
            System.out.println("out of range.... ");
        }
    }
}