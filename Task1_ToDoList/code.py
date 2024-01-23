#====================================================================================================================#
# a program to make the the 'To do list' :
# the program contains the following options or functions 
# 1- display Options
# 2- add tasks to a list
# 3- mark task as complete
# 4- view tasks 
# 5- quit
#====================================================================================================================#


#====================================================================================================================#
                                            # Global Variables #
#====================================================================================================================#

# define a list that will contain the tasks entered by the user with some initial values 
Tasks = [{"task":"Quran",    "Completed":True},
         {"task":"Salah",    "Completed":True}, 
         {"task":"Study",    "Completed":False},
         {"task":"Exercise", "Completed":True}, 
         {"task":"Sleep",    "Completed":False},
         {"task":"Visit Dad","Completed":True}]


#====================================================================================================================#
                                            # Functions Definition #
#====================================================================================================================#

# Main Code
def main():
    displayOptions()
    # run the program forever until the user quit  
    while(True):
        choice = input("Enter your choice : ")
        if(choice == '1'):
            addTask()
            displayOptions()
        elif(choice == '2'):
            markTaskAsComplete()
            displayOptions()
        elif(choice == '3'):
            viewTasks()
            displayOptions()
        elif(choice == '4'):
            print("Quiting program....") 
            break
        else:
            print("====================== ======================")
            print("Invalid Input!, please Enter between 1 and 4")
            print("====================== ======================")

# a function to add a task in the list of tasks
def addTask():
    # get the new task from the user 
    newTask = input("Enter Task you want to add : ")
    # make information about the task to add it in the list of tasks 
    newTaskInfo = {"task":newTask,"Completed":False}
    # add the new task to the list of tasks 
    Tasks.append(newTaskInfo)
    print("Task added successfully!")

# a function to mark the task as complete 
def markTaskAsComplete():
    
    # check if the list is Empty 
    if(len(Tasks) == 0):
        print("!! List is Empty !!")
    else:
        checkIncomplete = 0
        # display the incomplete tasks 
        print("Incomplete Tasks : ")
        for task in Tasks:
            if(task["Completed"] == False):
                print(f"Task Name: {task['task']}")
                checkIncomplete = 1
        
        # check if there is an incomplete task 
        if checkIncomplete == 0:
            print(" !! No Incomplete Task !! ")
        else:
            # get the task key
            taskName = input("Enter the task that is complete : ")
            flag = 0
            # change the task status from False to True 
            for task in Tasks:
                if(taskName == task["task"]):
                    task["Completed"] = True
                    flag = 1
                    print("Task Marked as Completed successfully")
            if flag == 0:
                print("!!!! Task Not Found !!!!")             

# a function to view the current tasks in the list 
def viewTasks():
    # check if the List of tasks is empty or not 
    if(not Tasks):
        print("!! List is Empty !!")
    else:
      
        for i in Tasks: 
            status = "✔️" if i["Completed"] else "❌"
            # print Task : Task Name     status    
            print(f"Task Name: {i['task']}     {status}")
    
# a function to display the options 
def displayOptions():
    # make a variable that contain the list of options that user can choose from 
    options = """    1- add tasks to a list
    2- mark task as complete
    3- view tasks 
    4- quit"""
    # display the list of options
    print("====================== ======================")
    print(options)
    print("====================== ======================")


if(__name__ == "__main__"):
    # Call main  
    main()
    
