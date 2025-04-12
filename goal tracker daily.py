# Daily Goal Tracker

def add_goal(goals_list):
    """User se naya goal add karne ka function"""
    goal_name = input("Enter your goal (e.g., Study Python): ")
    goals_list.append({"name": goal_name, "status": "Pending"})
    print(f"Goal '{goal_name}' added successfully!")

def mark_goal(goals_list):
    """Goal ko complete ya pending mark karne ka function"""
    if not goals_list:
        print("No goals added yet!")
        return
    print("\nYour Goals:")
    for i, goal in enumerate(goals_list, 1):
        print(f"{i}. {goal['name']} - {goal['status']}")
    try:
        choice = int(input("Enter goal number to mark as complete: ")) - 1
        if 0 <= choice < len(goals_list):
            goals_list[choice]["status"] = "Completed"
            print(f"Goal '{goals_list[choice]['name']}' marked as completed!")
        else:
            print("Invalid number! Try again.")
    except ValueError:
        print("Please enter a number!")

def show_summary(goals_list):
    """Goals ka summary dikhane ka function"""
    if not goals_list:
        print("No goals added yet!")
        return
    completed = sum(1 for goal in goals_list if goal["status"] == "Completed")
    pending = len(goals_list) - completed
    
    print("\n===== Daily Goal Summary =====")
    print(f"Total Goals: {len(goals_list)}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    print("\nDetails:")
    for i, goal in enumerate(goals_list, 1):
        print(f"{i}. {goal['name']} - {goal['status']}")
    
    # Motivational message
    if completed == len(goals_list):
        print("\nWow! You smashed all your goals! Keep shining! 🌟")
    elif completed > 0:
        print("\nGreat job! You're making progress, keep it up! 💪")
    else:
        print("\nDon't worry, start small and crush those goals! 🚀")

def main():
    """Main program loop"""
    goals_list = []  # Goals ko store karne ke liye list
    print("🎯 Welcome to Daily Goal Tracker! 🎯")
    print("Track your daily goals and stay productive!")
    
    while True:
        print("\nOptions:")
        print("1. Add a new goal")
        print("2. Mark a goal as complete")
        print("3. Show summary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_goal(goals_list)
        elif choice == "2":
            mark_goal(goals_list)
        elif choice == "3":
            show_summary(goals_list)
        elif choice == "4":
            print("Thanks for using Daily Goal Tracker! Keep hustling! 😎")
            break
        else:
            print("Invalid choice! Please pick 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()