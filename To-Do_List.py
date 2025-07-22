import json

class Task:
    


    def __init__(self):
        self.task = {}
       
       
    def addTask(self , Title, Description, Priority):
        if not Title:
            raise ValueError("Title cannot be empty")
        if not Description or not isinstance(Description, str):
            raise ValueError("Description cannot be empty") 
        if not isinstance(Priority, int) or not (0 <= Priority <= 5): 
            raise ValueError("Priority must be an integer between 0 and 5")
        self.task[Title] = {"Description": Description,"Priority": Priority}
        

    def viewTasks(self):
       with open("tasks.json", "r") as f:
         data = json.load(f)
         print(data)
            

    def markTaskAsDone(self, Title, Description):
        self.task[Title]["Description"] = Description
    
    def changePriority(self, Title, priority):
        self.task[Title][1] = priority
    
    def deleteTask(self, Title):
        del(self.task[Title])

    def saveToFile(self):
        with open("tasks.json", "w+") as file:
            json.dump(self.task, file, indent=4)

f = True
task1 = Task()
while f:
    
    print("1-Add a Task")
    print("2-View Tasks from File")
    print("3-Change Description")
    print("4-Change Priority")
    print("5-Delete Task")
    print("6-Exit Program")
    print("7-Save")

    try:
        operation = int(input("Enter your operation: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  
    
    match operation:
        case 1: 
            Title = input("enter the Title of Task ")
            if not Title:
                print("Title cannot be empty")
                continue
            Description = input("Enter Description ")
            if not Description:
                print("Description cannot be empty")
                continue
            try:
                Priority = int(input("Enter the Priority from 0 to 5 "))
                if not (0 <= Priority <= 5):
                    print("Priority must be an integer between 0 and 5")
                    continue
            except ValueError:
                print("Invalid input! Please enter an integer for priority.")
                continue
            task1.addTask(Title, Description, Priority)
        case 2:
            if not task1.task:
                print("No tasks available")
                continue
            with open("tasks.json", "r+") as file:
                if file.read().strip():
                    task1.viewTasks()
                else:
                    print("No tasks available")
                continue
        case 3:
            Title = input("Enter the title of task to change ")
            if Title not in task1.task:
                print("Task not found")
                continue
            Description = input("Enter the Description ")
            if not Description:
                print("Description cannot be empty")
                continue
            task1.markTaskAsDone(Title, Description)
        case 4:
            Title = input("Enter the title of task to change ")
            if Title not in task1.task:
                print("Task not found")
                continue
            try:
                Priority = int(input("Enter the Priority from 0 to 5 "))
                if not (0 <= Priority <= 5):
                    print("Priority must be an integer between 0 and 5")
                    continue
            except ValueError:
                print("Invalid input! Please enter an integer for priority.")
                continue
            task1.changePriority(Title, Priority)
        case 5:
            Title = input("Enter the title of task to delete ")
            if Title not in task1.task:
                print("Task not found")
                continue
            task1.deleteTask(Title)
        case 6: f = False
        case 7: task1.saveToFile()
        case _:
            print("Invalid operation, please try again")
            continue 

            
        
    
   

            
            

    





        