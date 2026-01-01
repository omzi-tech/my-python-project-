import java.util.ArrayList;
import java.util.Scanner;

class Flight {
     String flightNumber;
     String departureTime;
     String arrivalTime;
     String status;

    public Flight(String flightNumber, String departureTime, String arrivalTime, String status) {
        this.flightNumber = flightNumber;
        this.departureTime = departureTime;
        this.arrivalTime = arrivalTime;
        this.status = status;
    }

    public String getFlightNumber() {
        return flightNumber;
    }

    public String getDepartureTime() {
        return departureTime;
    }

    public String getArrivalTime() {
        return arrivalTime;
    }

    public String getStatus() {
        return status;
    }

    @Override
    public String toString() {
        return "Flight Number: " + flightNumber + ", Departure Time: " + departureTime + ", Arrival Time: " + arrivalTime + ", Status: " + status;
    }
}

class FlightManager {
    private ArrayList<Flight> flights;

    public FlightManager() {
        flights = new ArrayList<>();
    }

    public void addFlight(Flight flight) {
        flights.add(flight);
    }

    public ArrayList<Flight> getFlights() {
        return flights;
    }
}

class FlightInfoDisplay {
    public void displayFlights(ArrayList<Flight> flights) {
        for (Flight flight : flights) {
            System.out.println(flight);
        }
    }
}

public class FlightInformationSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        FlightManager flightManager = new FlightManager();
        FlightInfoDisplay flightInfoDisplay = new FlightInfoDisplay();

        while (true) {
            System.out.println("Welcome to the Flight Information System");
            System.out.print("Enter flight number or type 'exit' to quit: ");
            String flightNumber = scanner.nextLine();
            if (flightNumber.equalsIgnoreCase("exit")) {
                break;
            }
            System.out.print("Enter departure time: ");
            String departureTime = scanner.nextLine();
            System.out.print("Enter arrival time: ");
            String arrivalTime = scanner.nextLine();
            System.out.print("Enter flight status: ");
            String status = scanner.nextLine();

            Flight flight = new Flight(flightNumber, departureTime, arrivalTime, status);
            flightManager.addFlight(flight);

            System.out.println("Current Flights:");
            flightInfoDisplay.displayFlights(flightManager.getFlights());
        }

        scanner.close();
    }
}
