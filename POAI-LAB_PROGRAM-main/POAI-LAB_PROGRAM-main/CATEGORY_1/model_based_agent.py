# Model Based Agent - Parking Gate System

parking_slots = 5      # Internal Model (Memory)
max_slots = 5

def parking_gate(vehicle):
    global parking_slots

    print("\n------ Parking Gate System ------")

    if vehicle == "entry":
        print("Percept : Vehicle at Entry Gate")

        if parking_slots > 0:
            parking_slots -= 1
            print("Action  : Open Entry Gate")
            print("Action  : Allocate Parking Slot")
            print("Action  : Close Entry Gate")
            print("Status  : Vehicle Parked")
            print("Available Slots :", parking_slots)
        else:
            print("Action  : Keep Gate Closed")
            print("Status  : Parking Full")

    elif vehicle == "exit":
        print("Percept : Vehicle at Exit Gate")

        if parking_slots < max_slots:
            parking_slots += 1
            print("Action  : Open Exit Gate")
            print("Action  : Update Parking Slots")
            print("Action  : Close Exit Gate")
            print("Status  : Vehicle Exited")
            print("Available Slots :", parking_slots)
        else:
            print("Status  : Parking Already Empty")

    else:
        print("Invalid Input!")


# Main Program
while True:

    print("\n====== Parking Gate Menu ======")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. View Available Slots")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        parking_gate("entry")

    elif choice == "2":
        parking_gate("exit")

    elif choice == "3":
        print("\n------ Parking Status ------")
        print("Available Parking Slots :", parking_slots)
        print("Occupied Parking Slots  :", max_slots - parking_slots)

    elif choice == "4":
        print("System Shutdown.")
        break

    else:
        print("Invalid Choice! Please try again.")