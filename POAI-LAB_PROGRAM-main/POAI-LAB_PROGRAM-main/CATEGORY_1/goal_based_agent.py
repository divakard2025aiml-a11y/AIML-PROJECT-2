# Goal Based Agent - Smart Irrigation System

def irrigation_system(condition):

    print("\n------ Smart Irrigation System ------")

    if condition == "dry":
        print("Percept : Soil is Dry")
        print("Goal     : Maintain Healthy Soil Moisture")
        print("Action   : Turn Water Pump ON")
        print("Action   : Irrigate the Field")
        print("Action   : Turn Water Pump OFF")
        print("Status   : Goal Achieved")

    elif condition == "wet":
        print("Percept : Soil is Wet")
        print("Goal     : Save Water")
        print("Action   : Keep Water Pump OFF")
        print("Status   : Goal Achieved")

    elif condition == "rain":
        print("Percept : Rain Detected")
        print("Goal     : Avoid Water Wastage")
        print("Action   : Stop Irrigation")
        print("Status   : Goal Achieved")

    else:
        print("Invalid Input!")


# Main Program

while True:

    print("\n====== Smart Irrigation Menu ======")
    print("1. Dry Soil")
    print("2. Wet Soil")
    print("3. Rain Detected")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        irrigation_system("dry")

    elif choice == "2":
        irrigation_system("wet")

    elif choice == "3":
        irrigation_system("rain")

    elif choice == "4":
        print("System Shutdown.")
        break

    else:
        print("Invalid Choice! Please try again.")