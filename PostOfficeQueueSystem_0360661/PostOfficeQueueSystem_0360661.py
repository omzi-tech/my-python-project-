bill_payment_queue = []
license_renew_queue = []
counters = {
    "Counter 1": "No ticket",
    "Counter 2": "No ticket",
    "Counter 3": "No ticket",
    "Counter 4": "No ticket",
}
bill_payment_ticket_number = 1001
license_renew_ticket_number = 2001

def issue_new_ticket(ticket_type):
    global bill_payment_ticket_number  
    if ticket_type == "bill_payment":
        new_ticket_number = bill_payment_ticket_number
        bill_payment_queue.append(new_ticket_number)
        bill_payment_ticket_number += 1
        return new_ticket_number
    elif ticket_type == "license_renew":
        new_ticket_number = license_renew_ticket_number
        license_renew_queue.append(new_ticket_number)
        license_renew_ticket_number += 1
        return new_ticket_number
    else:
        return None

def assign_ticket_to_counter(counter_number, ticket_type):
    if ticket_type == "bill_payment":
        if counter_number in [1, 2]:
            if bill_payment_queue:
                ticket_number = bill_payment_queue.pop(0)
                old_ticket_number = counters[f"Counter {counter_number}"]
                counters[f"Counter {counter_number}"] = ticket_number
                print(f"Assigned ticket {ticket_number} for bill payment to Counter {counter_number}")
                if old_ticket_number != "No ticket":
                    print(f"Replaced ticket {old_ticket_number} at Counter {counter_number}")
            else:
                print(f"No tickets in queue for bill payment at Counter {counter_number}")
        else:
            print("Invalid counter number for bill payment")
    elif ticket_type == "license_renew":
        if counter_number in [3, 4]:
            if license_renew_queue:
                ticket_number = license_renew_queue.pop(0)
                old_ticket_number = counters[f"Counter {counter_number}"]
                counters[f"Counter {counter_number}"] = ticket_number
                print(f"Assigned ticket {ticket_number} for license renew to Counter {counter_number}")
                if old_ticket_number != "No ticket":
                    print(f"Replaced ticket {old_ticket_number} at Counter {counter_number}")
            else:
                print(f"No tickets in queue for license renew at Counter {counter_number}")
        else:
            print("Invalid counter number for license renew")
    else:
        print("Invalid ticket type")

def display_queue_status():
    print("Ticket in queue for Bill Payment:", bill_payment_queue)
    print("Ticket in queue for License Renew:", license_renew_queue)
    print("Tickets at Counters:", counters)

def start():
    while True:
        print("Enter 0 to 5 for the following options:")
        print("0 → Issue a new ticket for a customer")
        print("1 → Assign ticket in the queue for bill payment to Counter 1")
        print("2 → Assign ticket in the queue for bill payment to Counter 2")
        print("3 → Assign ticket in the queue for license renew to Counter 3")
        print("4 → Assign ticket in the queue for license renew to Counter 4")
        print("5 → Quit program")

        display_queue_status()

        option = int(input("Enter your option: "))
        if option == 0:
            print("Please enter the type of service:")
            print("1 → Bill Payment")
            print("2 → License Renewal")
            ticket_type = int(input("Enter the service type (1 or 2): "))
            if ticket_type == 1:
                new_ticket_number = issue_new_ticket("bill_payment")
                if new_ticket_number is not None:
                    print("New ticket number for Bill Payment:", new_ticket_number)
                else:
                    print("Invalid service type. Please enter 1 for Bill Payment or 2 for License Renewal.")
            elif ticket_type == 2:
                new_ticket_number = issue_new_ticket("license_renew")
                if new_ticket_number is not None:
                    print("New ticket number for License Renewal:", new_ticket_number)
                else:
                    print("Invalid service type. Please enter 1 for Bill Payment or 2 for License Renewal.")
            else:
                print("Invalid service type. Please enter 1 for Bill Payment or 2 for License Renewal.")
        elif option in [1, 2, 3, 4]:
            counter_number = option
            ticket_type = "bill_payment" if counter_number in [1, 2] else "license_renew"
            assign_ticket_to_counter(counter_number, ticket_type)
        elif option == 5:
            print("Quitting program...")
            break
        else:
            print("Invalid option, try again...")

start()
