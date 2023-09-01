# Define a class named 'Task' to represent individual tasks
class Task:
    # Constructor method to initialize task attributes (name, description, isDone)
    def __init__(self, name, description, isDone=False):
        self.name = name  # Initialize the task name attribute
        self.description = description  # Initialize the task description attribute
        # Initialize the task status attribute (default is not done)
        self.isDone = isDone


# Define a function to create a new task and add it to the task list
def createTask():
    # Prompt the user to input task details (name, description, and whether it's done)
    name = input("Please write a name: ")  # Read the task name from the user
    # Read the task description from the user
    description = input("Please write a description: ")
    # Read if the task is done from the user and convert to a boolean value
    isDone = input("Is it done? (yes/no): ").lower() == "yes"

    # Create a new task object using the Task class constructor
    new_task = Task(name, description, isDone)
    # Append the new task to the list of tasks
    my_tasks.append(new_task)


# Define a function to display all the tasks in the task list
def showAllTasks(my_tasks):
    print("Created tasks:")
    # Iterate through the list of tasks
    for task in my_tasks:
        # Display task details (name, description, and whether it's done)
        print(f"Name: {task.name}")  # Display the task name
        # Display the task description
        print(f"Description: {task.description}")
        # Display whether the task is marked as done or not
        print(f"Is Done: {'Yes' if task.isDone else 'No'}")
        print()


# Initialize an empty list to store tasks
my_tasks = []

# Display the current list of tasks (empty at the beginning)
print("Current tasks: " + str(my_tasks))

# Call the createTask function to add a new task to the list
createTask()

# Call the showAllTasks function to display all tasks in the list (including the newly added one)
showAllTasks(my_tasks)
