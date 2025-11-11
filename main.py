
#Example of how Database would look like.
# Would ideally have more entires and be updatable dynamically.
database = [
    ["ORD001", "Ali Alaparmak", "Out for delivery", "Dallas, TX", "ETA: 20 minutes"],
    ["ORD002", "Sara Kaya", "Delivered", "Plano, TX", "Delivered yesterday"],
    ["ORD003", "Omar Hamdy", "Processing at warehouse", "Houston, TX", "ETA: 2 days"],
    ["ORD004", "Lina Hassan", "Shipped", "Austin, TX", "ETA: Tomorrow morning"],
    ["ORD005", "Emily Chen", "Pending payment confirmation", "Frisco, TX", "ETA: TBD"]
]

def greet_user():
    fname = input("Please enter your full name: ")
    print(f"Hello, {fname.split()[0]}! Welcome to Elite 101.")
    return fname

def track_order(order_n):
    if order_n == "NONE":
        print("You have chosen not to track an order.")
        while order_n not in [order[0] for order in database]:
            order_n = input("Please enter your six character order number to track your order: ").strip().upper()
    for order in database:
        if order[0] == order_n:
            print(f"Order Status: {order[2]}")
            print(f"Location: {order[3]}")
            print(f"Estimated Time of Arrival: {order[4]}")
            return
    print("Order not found. Please check your order number.")

def contact_support(order_n, review, general_review=""):
    print("Connecting you to customer support... Please wait.")
    print("You are now connected to a customer support representative.")

def main():
    greet_user()
    order_n = ""
    valid_orders = [order[0] for order in database]

    while True:
        order_n = input("Enter your 6-character order number (or type NONE if you don’t have one): ").strip().upper()
        if order_n == "NONE" or order_n in valid_orders:
            break
        print("That order number wasn’t found. Please try again.")
    
    print("Thank you! How can we assist you today?")


    while True:
        print("1. Track my order")
        print("2. Request a refund")
        print("3. Contact customer support")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            track_order(order_n)
        elif choice == "2":
            general_review = input("Please provide general feedback about your experience. Examples (Damaged/Defectgive, Wrong Item, Arrived Late, Changed mind, Other): ")
            review = input("Please provide a reason for the refund: ")
            print("Your refund request has been submitted.")
            print("A customer support representative will contact you shortly.")
            contact_support(order_n,review, general_review)
        elif choice == "3":
            reason = input("Please provide a reason for contacting support: ")
            contact_support(order_n,reason)
        elif choice == "4":
            print("Thank you for contacting our support team.")
            print("Have a Good Day")
            break
        else:
            print("Enter a valid choice:")

if __name__ == "__main__":
    main()
