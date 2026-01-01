import java.util.Random;
import java.util.Scanner;

public class GradingSystem {

    // Method to get student information
    public static String[] getStudentInfo() {
        Scanner scanner = new Scanner(System.in);
        String[] info = new String[5];

        System.out.print("Enter student's name: ");
        info[0] = scanner.nextLine();

        System.out.print("Enter student ID: ");
        info[1] = scanner.nextLine();

        System.out.print("Enter marks for Math: ");
        info[2] = scanner.nextLine();

        System.out.print("Enter marks for Computer Science: ");
        info[3] = scanner.nextLine();

        System.out.print("Enter marks for English: ");
        info[4] = scanner.nextLine();

        return info;
    }

    // Method to apply bonus marks
    public static int[] applyBonusMarks(int[] marks) {
        Random rand = new Random();
        for (int i = 0; i < marks.length; i++) {
            int bonus = rand.nextInt(6); // 0 to 5
            marks[i] = Math.min(marks[i] + bonus, 100);
        }
        return marks;
    }

    // Method to calculate grade
    public static char calculateGrade(int[] marks) {
        int total = 0;
        for (int mark : marks) {
            total += mark;
        }
        double average = total / 3.0;

        if (average >= 90) {
            return 'A';
        } else if (average >= 80) {
            return 'B';
        } else if (average >= 70) {
            return 'C';
        } else if (average >= 60) {
            return 'D';
        } else {
            return 'F';
        }
    }

    // Method to provide feedback
    public static void provideFeedback(char grade) {
        switch (grade) {
            case 'A':
                System.out.println("Feedback: Excellent");
                break;
            case 'B':
                System.out.println("Feedback: Good");
                break;
            case 'C':
                System.out.println("Feedback: Satisfactory");
                break;
            case 'D':
                System.out.println("Feedback: Needs Improvement");
                break;
            case 'F':
                System.out.println("Feedback: Fail");
                break;
            default:
                System.out.println("Feedback: Invalid grade");
                break;
        }
    }

    // Main method
    public static void main(String[] args) {
        String[] studentInfo = getStudentInfo();
        int[] marks = new int[3];

        for (int i = 2; i < 5; i++) {
            marks[i - 2] = Integer.parseInt(studentInfo[i]);
        }

        marks = applyBonusMarks(marks);

        System.out.println("Calculating final marks...");
        System.out.println("Math (after bonus): " + marks[0]);
        System.out.println("Computer Science (after bonus): " + marks[1]);
        System.out.println("English (after bonus): " + marks[2]);

        char grade = calculateGrade(marks);
        double average = (marks[0] + marks[1] + marks[2]) / 3.0;
        System.out.println("Average Marks: " + average);
        System.out.println("Final Grade: " + grade);

        provideFeedback(grade);
    }
}
