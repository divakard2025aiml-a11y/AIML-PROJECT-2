# Utility-Based Agent - Music Recommendation System

def music_recommendation(mood):

    print("\n------ Music Recommendation System ------")

    if mood == "happy":
        print("Percept : User is Happy")
        print("Utility : Best Listening Experience")
        print("Action  : Recommend Pop Songs")
        print("Status  : Recommendation Completed")

    elif mood == "sad":
        print("Percept : User is Sad")
        print("Utility : Improve User Mood")
        print("Action  : Recommend Motivational Songs")
        print("Status  : Recommendation Completed")

    elif mood == "relaxed":
        print("Percept : User Wants to Relax")
        print("Utility : Peaceful Listening Experience")
        print("Action  : Recommend Soft Melody Songs")
        print("Status  : Recommendation Completed")

    elif mood == "workout":
        print("Percept : User is Working Out")
        print("Utility : Increase Energy")
        print("Action  : Recommend Workout Songs")
        print("Status  : Recommendation Completed")

    else:
        print("Invalid Input!")


# Main Program

while True:

    print("\n====== Music Recommendation Menu ======")
    print("1. Happy Mood")
    print("2. Sad Mood")
    print("3. Relaxed Mood")
    print("4. Workout Mood")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        music_recommendation("happy")

    elif choice == "2":
        music_recommendation("sad")

    elif choice == "3":
        music_recommendation("relaxed")

    elif choice == "4":
        music_recommendation("workout")

    elif choice == "5":
        print("System Shutdown.")
        break

    else:
        print("Invalid Choice! Please try again.")