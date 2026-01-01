def assign_ticket_to_counter(bill_payment_queue, license_renew_queue, counters, ticket_type):
    if ticket_type == "bill_payment":
        if not bill_payment_queue:
            raise ValueError("No tickets in queue for bill payment")
        
        ticket_number = bill_payment_queue.pop(0)
        counter_number = "Counter 1" if counters["Counter 1"] == "No ticket" else "Counter 2"
        counters[counter_number] = ticket_number
        print(f"Assigned ticket {ticket_number} for bill payment to {counter_number}")

    elif ticket_type == "license_renew":
        if not license_renew_queue:
            raise ValueError("No tickets in queue for license renew")
        
        ticket_number = license_renew_queue.pop(0)
        counter_number = "Counter 3" if counters["Counter 3"] == "No ticket" else "Counter 4"
        counters[counter_number] = ticket_number
        print(f"Assigned ticket {ticket_number} for license renew to {counter_number}")

def display_queue_status(bill_payment_queue, license_renew_queue, counters):
    print("Ticket in queue for Bill Payment:", bill_payment_queue)
    print("Ticket in queue for License Renew:", license_renew_queue)
    print("Tickets at Counters:", counters)

def start():
    bill_payment_queue = []
    license_renew_queue = []
    counters = {
        "Counter 1": "No ticket",
        "Counter 2": "No ticket",
        "Counter 3": "No ticket",
        "Counter 4": "No ticket",
    }
    next_bill_payment_number = 1001  
    next_license_number = 2001  

    while True:
        print("Enter 0 to 5 for the following options:")
        print("0 → Issue a new ticket for a customer")
        print("1 → Assign ticket in the queue for bill payment to Counter 1")
        print("2 → Assign ticket in the queue for bill payment to Counter 2")
        print("3 → Assign ticket in the queue for license renew to Counter 3")
        print("4 → Assign ticket in the queue for license renew to Counter 4")
        print("5 → Quit program")

        display_queue_status(bill_payment_queue, license_renew_queue, counters)

        option = int(input("Enter your option: "))
        if option == 0:
            print("Please enter the type of service:")
            print("1 → Bill Payment")
            print("2 → License Renewal")
            ticket_type = input("Enter the service type (1 or 2): ")
            if ticket_type == "1":
                bill_payment_queue.append(next_bill_payment_number)
                next_bill_payment_number += 1
            elif ticket_type == "2":
                license_renew_queue.append(next_license_number)
                next_license_number += 1
            else:
                print("Invalid service type. Please enter 1 for Bill Payment or 2 for License Renewal.")
        elif option in [1, 2]:
            assign_ticket_to_counter(bill_payment_queue, license_renew_queue, counters, "bill_payment")
        elif option in [3, 4]:
            assign_ticket_to_counter(bill_payment_queue, license_renew_queue, counters, "license_renew")
        elif option == 5:
            print("Quitting program...")
            break
        else:
            print("Invalid option, try again...")

if __name__ == "__main__":
    start()
