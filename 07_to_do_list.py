# Simple To-Do List Application

def display_todo_list(todo_list):
    """Display all items in the to-do list"""
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\n=== Your To-Do List ===")
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item}")

def add_item(todo_list, item):
    """Add a new item to the to-do list"""
    todo_list.append(item)
    print(f"Added: {item}")

def remove_item(todo_list, index):
    """Remove an item from the to-do list by index"""
    if 1 <= index <= len(todo_list):
        removed_item = todo_list.pop(index - 1)
        print(f"Removed: {removed_item}")
    else:
        print("Invalid index! Please enter a valid number.")

def save_to_file(todo_list, filename="todo_list.txt"):
    """Save the to-do list to a file"""
    try:
        with open(filename, 'w') as file:
            for item in todo_list:
                file.write(item + '\n')
        print(f"To-do list saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_from_file(filename="todo_list.txt"):
    """Load the to-do list from a file"""
    todo_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                todo_list.append(line.strip())
        print(f"To-do list loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty list.")
    except Exception as e:
        print(f"Error loading file: {e}")
    return todo_list

def main():
    print("=== Simple To-Do List Manager ===")
    
    # Load existing to-do list
    todo_list = load_from_file()
    
    while True:
        print("\nOptions:")
        print("1. View to-do list")
        print("2. Add item")
        print("3. Remove item")
        print("4. Save to file")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            display_todo_list(todo_list)
            
        elif choice == '2':
            item = input("Enter the item to add: ")
            if item.strip():  # Don't add empty items
                add_item(todo_list, item)
            else:
                print("Please enter a valid item!")
                
        elif choice == '3':
            display_todo_list(todo_list)
            if todo_list:
                try:
                    index = int(input("Enter the number of the item to remove: "))
                    remove_item(todo_list, index)
                except ValueError:
                    print("Please enter a valid number!")
                    
        elif choice == '4':
            save_to_file(todo_list)
            
        elif choice == '5':
            # Ask if user wants to save before exiting
            if todo_list:
                save_choice = input("Save your to-do list before exiting? (yes/no): ").lower()
                if save_choice in ['yes', 'y']:
                    save_to_file(todo_list)
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()