# Simple Reflex Agent - Smoke Detector System

def smoke_detector(smoke):
    print("\n----- Smoke Detection System -----")

    if smoke == "yes":
        print("Percept : Smoke Detected")
        print("Action  : Turn Alarm ON")
        print("Action  : Activate Water Sprinklers")
        print("Action  : Notify Fire Department")
        print("Status  : Emergency")

    elif smoke == "no":
        print("Percept : No Smoke Detected")
        print("Action  : Alarm OFF")
        print("Action  : Continue Monitoring")
        print("Status  : Safe")

    else:
        print("Invalid Input!")


# Main Program
while True:
    print("\n====== Smoke Detector Menu ======")
    print("1. Smoke Detected")
    print("2. No Smoke")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        smoke_detector("yes")

    elif choice == "2":
        smoke_detector("no")

    elif choice == "3":
        print("System Shutdown.")
        break

    else:
        print("Invalid Choice! Please try again.")