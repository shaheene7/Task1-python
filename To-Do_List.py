class Task:
    task = {}


    def __init__(self):
        pass

    def addTask(self , Title, Description, Priority):
        self.title = Title
        self.description = Description
        self.priority = Priority
        self.task.update({Title: [Description, Priority]})

    def viewTasks(self):
        for key,values in self.task.items():
            print(f"Title: {key}, Status: {values[0]}\n")
            

    def markTaskAsDone(self, Title, Status):
        self.task[Title][0] = Status
    
    def changePriority(self, Title, priority):
        self.task[Title][1] = priority
    
    def deleteTask(self, Title):
        del(self.task[Title])

    def saveToFile(self):
        fo = open("tasks.json", "w+")
        fo.seek(0)
        r = fo.readline()
        if not r:
          fo.write("[\n")
        for key,values in self.task.items():
            fo.seek(0,2)
            fo.write("{")
            fo.write(f'"Title": "{key}",\n "Description": "{values[0]}",\n "Priority": {values[1]}\n')
            fo.write("},\n")
            
        fo.write("]")
        fo.close()

f = True
task1 = Task()
while f:
    
    print("1-Add a Task")
    print("2-View Tasks")
    print("3-Change Status")
    print("4-Change Priority")
    print("5-Delete Task")
    print("6-Exit Program")
    print("7-Save")
    in1 = int(input("Enter your operation "))
    
    match in1:
        case 1: 
            Title = input("Enter the Title of Task ")
            Description = input("Enter Status ")
            Priority = int(input("Enter the Priority from 0 to 5 "))
            task1.addTask(Title, Description, Priority)
        case 2: task1.viewTasks()
        case 3:
            Title = input("Enter the title of task to change ")
            Status = input("Enter the status ")
            task1.markTaskAsDone(Title, Status)
        case 4:
            Title = input("Enter the title of task to change ")
            Priority = input("Enter the Priority from 0 to 5 ")
            task1.changePriority(Title, Priority)
        case 5:
            Title = input("Enter the title of task to delete ")
            task1.deleteTask(Title)
        case 6: f = False
        case 7: task1.saveToFile()
        case _: 
            print("invalid input")
            break
        
    
   

            
            

    





        