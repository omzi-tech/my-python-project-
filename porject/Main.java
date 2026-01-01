import java.util.Scanner;

public class Main {

    static class Employee {
        String name;
        int employeeId;
        String department;

        public Employee(String name, int employeeId, String department) {
            this.name = name;
            this.employeeId = employeeId;
            this.department = department;
        }

        public void displayEmployeeDetails() {
            System.out.println("Employee details: " + name + ", " + employeeId + ", " + department);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Employee[] employees = new Employee[5];

        for (int i = 0; i < employees.length; i++) {
            System.out.println("Enter details for employee " + (i + 1) + ":");

            System.out.print("Name: ");
            String name = scanner.nextLine();

            System.out.print("Employee ID: ");
            int employeeId = scanner.nextInt();

            scanner.nextLine(); 
            
            System.out.print("Department: ");
            String department = scanner.nextLine();

            employees[i] = new Employee(name, employeeId, department);
        }

        System.out.println("\nEmployee Details:");
        for (Employee employee : employees) {
            employee.displayEmployeeDetails();
        }

        scanner.close();
    }
}
