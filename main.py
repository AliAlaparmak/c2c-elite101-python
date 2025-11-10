
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""
database = [
    ["ORD001", "Ali Alaparmak", "Out for delivery", "Dallas, TX", "ETA: 20 minutes"]
]

def greet_user():
    fname = input("Please enter your full name: ")
    print(f"Hello, {fname.split()[0]}! Welcome to Elite 101.")
    return fname

def track_order(order_n):
    for order in database:
        if order[0] == order_n:
            print(f"Order Status: {order[2]}")
            print(f"Location: {order[3]}")
            print(f"Estimated Time of Arrival: {order[4]}")
            return
    print("Order not found. Please check your order number.")

def contact_support(order_n):
    print("Connecting you to customer support... Please wait.")
    print("You are now connected to a customer support representative.")

def main():
    greet_user()
    order_n = input("Please enter your six character order number: ").strip().upper()

    while True:
        print("What would you like to do?")
        print("1. Track my order")
        print("2. Request a refund")
        print("3. Contact customer support")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            track_order(order_n)
        elif choice == "2":
            contact_support(order_n)
        elif choice == "3":
            contact_support(order_n)
        elif choice == "4":
            print("Have a Good Day")
            break
        else:
            print("Enter a valid choice:")

if __name__ == "__main__":
    main()
