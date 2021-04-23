#declare lists to use later

details = []
users = []
user = []
passwords = []

#define function reg_user
def reg_user():
    reoccuring = False
    newU = input("Please enter your new username: \n")
    newP = input("Please enter a new password: \n")
    confirmed = input("Please confirm your password:\n")
    if confirmed == newP:
        newdetails = "\n" + newU+ ", " +newP
        with open("user.txt","r") as F:
            for line in F:
                while newU in line:
                    print("You have entered a username that already exists. Please enter a valid username and password: \n")
                    newU = input("Please enter your new username: \n")
                    newP = input("Please enter a new password: \n")
                    confirmed = input("Please confirm your password:\n")
                    newdetails = "\n" + newU+ ", " +newP
        with open("user.txt", "a") as f:
            f.write("\n")
            f.write(newdetails)
                        
                    
#define function add_task
def add_task():
    which_user = input("Please enter the username of the person you'd like to assign a task: \n")
    title = input("Please enter the title of the task: \n")
    descr = input("Please enter a description of the task: \n")
    current_date = input("please enter todays date: \n")
    due_date = input("Please enter the due date of the task: \n")
    complete = "No"
    newtask = which_user +", "+ title +", "+ descr+ ", "+ current_date+", " +due_date+", "+ complete
    #open in append mode
    with open("tasks.txt","a+") as f:
        f.write("\n")
        f.write(newtask)
#define view_all fucnction
def view_all():
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.split(', ')
            print("{0:15}{1}".format("task: ",line[1]))
            print("{0:15}{1}".format("Assigned to:",line[0]))
            print("{0:13}{1}".format("Date assigned: ",line[3]))
            print("{0:15}{1}".format("Due date: ",line[4]))
            print("{0:7}{1}".format("Task complete: ",line[5]))
            print("{0:7}{1}".format("Task description: ",line[2]))
            print("\n")
#define view_mine
def view_mine():
    #define variables needed
    counter = -1
    lis = []
    dictionary = {}
    print("To select a specific task enter a number, or enter '-1' to return to the main menu\n")
    with open("tasks.txt", "r") as f:
        print("Your tasks are: \n")
        for line in f:
            line = line.split(',')
            #increment count by 1 for each line
            counter += 1
            # check if username matches with the task.
            if username == line[0]:
                print(counter)
                print("{0:15}{1}".format("task: ",line[1]))
                print("{0:13}{1}".format("Date assigned: ",line[3]))
                print("{0:15}{1}".format("Due date: ",line[4]))
                print("{0:7}{1}".format("Task complete: ",line[5]))
                print("{0:7}{1}".format("Task description: ",line[2]))
                print("\n")
        f.close()

    #open file again 
    with open("tasks.txt", "r") as f:
        comp = 0
        count = -1
        choice = int(input())
        for line in f:
            line.strip()
            line = line.rstrip()
            line = line.split(', ')
            count +=1
            #assign dictionary in the for loop
            dictionary[count] = line
            if choice == count:
                print("{0:15}{1}".format("task: ",dictionary[count][1]))
                print("{0:13}{1}".format("Date assigned: ",dictionary[count][3]))
                print("{0:15}{1}".format("Due date: ",dictionary[count][4]))
                print("{0:7}{1}".format("Task complete: ",dictionary[count][5]))
                print("{0:7}{1}".format("Task description: ",dictionary[count][2]))
                print("\n")

        #create while loop   
        while choice != -1:

            choice2 = input("to mark the task complete enter 'mark' to edit the task enter 'edit': \n")

            if choice2 == 'mark':
                #if yes, then print
                dictionary[choice][5] = 'Yes'
                print("{0:15}{1}".format("task: ",dictionary[choice][1]))
                print("{0:13}{1}".format("Date assigned: ",dictionary[choice][3]))
                print("{0:15}{1}".format("Due date: ",dictionary[choice][4]))
                print("{0:7}{1}".format("Task complete: ",dictionary[choice][5]))
                print("{0:7}{1}".format("Task description: ",dictionary[choice][2]))
                print("\n")
                with open("tasks.txt","r") as f:
                        F = f.readlines()
                with open("tasks.txt", "w") as f:
                    for i in range(count+1):
                        F[i] = dictionary[i][0]+ ", " + dictionary[i][1] +", "+ dictionary[i][2]+ ", " + dictionary[i][3]+ ", " + dictionary[i][4]+ ", "+ dictionary[i][5]
                        f.write(F[i])
                        f.write("\n")
                    
            
            if choice2 == 'edit':
                if dictionary[choice][5] != 'Yes':
                    
                    dictionary[choice][0] = input("Please enter the username you'd like to reassign this task to: \n")
                    dictionary[choice][4] = input("please enter the due date of this task: \n")
                    print("{0:15}{1}".format("User: " ,dictionary[choice][0]))
                    print("{0:15}{1}".format("task: ",dictionary[choice][1]))
                    print("{0:13}{1}".format("Date assigned: ",dictionary[choice][3]))
                    print("{0:15}{1}".format("Due date: ",dictionary[choice][4]))
                    print("{0:7}{1}".format("Task complete: ",dictionary[choice][5]))
                    print("{0:7}{1}".format("Task description: ",dictionary[choice][2]))
                    print("\n")
                    
                    with open("tasks.txt","r") as f:
                        F = f.readlines()
                    with open("tasks.txt", "w") as f:
                        for i in range(count+1):
                            F[i] = dictionary[i][0]+ ", " + dictionary[i][1] +", "+ dictionary[i][2]+ ", " + dictionary[i][3]+ ", " + dictionary[i][4]+ ", "+ dictionary[i][5]
                            f.write(F[i])
                            f.write("\n")        
            
                        

            if choice2 == 'edit' and dictionary[count][5] == 'Yes':
                
                print("This task has already been completed, you can no longer edit it.")

            choice = int(input())


        
#define gen_rep()
def gen_rep():
    #define all necessary variables
    dates = []
    dates2 = []
    comp = 0
    complete = 0
    incomplete = 0
    incomp = 0
    datesd = {'Jan':1,'Feb': 2,'Mar':3, 'Apr':4, 'May':5 ,'Jun':6, 'Jul':7 ,'Aug':8,'Sep':9,'Oct':10,'Nov':11, 'Dec':12}
    currentmonth = 4
    currentday = 3
    currentyear = 2021
    overdue = 0
    usertasks = 0
    line_count = 0
    tasks = {}
    datess = {}
    Comp = []
    c = 0
    entry = ""
    numtask =""
    numcomp = ""
    numinc = ""
    D = {}

    #open task in read mode
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.rstrip()
            line = line.split(', ')
            if line[5] == 'Yes':
                comp += 1
            if line[5] == 'No':
                incomp += 1
            dates.append(line[4].split(" "))
            if line != "\n":
                line_count += 1.
        for i in dates:
            #first check if the task is incomplete
            if line[5] =='No':
                if int(i[2]) >= currentyear:
                    overdue +=1
                elif int(i[2])< currentyear:
                    if datesd[i[1]] > currentmonth and int(i[0])> currentday:
                        overdue +=1
                else:
                    overdue = 0
                

    #open in write mode to generate new text file
    with open("task_overview.txt","w") as t:
        perc = (overdue / line_count) * 100
        t.write("The total number of tasks is : {}".format(line_count))
        t.write("\n")
        t.write("The total number of completed tasks are {}".format(comp))
        t.write("\n")
        t.write("The total number of incomplete tasks are {}".format(incomp))
        t.write("\n")
        t.write("The total number of incomplete tasks that are overdue are {}".format(overdue))
        t.write("\n")
        t.write("The percentage of tasks that are overdue is: {} %".format(perc))
    #open file again in read mode to display on screen   
    with open("task_overview.txt", "r") as t:
        for line in t:
            print(line)

    with open("tasks.txt","r") as f:
        for line in f:
            line.rstrip()
            data = line.split(", ")[4]
            dataa = data.split(" ")
            userlist = line.split(', ')[0]
            tasklist = line.split(', ')[1]
            Com = line.split(", ")[5]
            Comp.append(Com.rstrip())
            dates2.append(data)
            if userlist not in tasks:
                tasks[userlist] = [tasklist] 
            else:
                tasks[userlist].append(tasklist)
            if userlist not in D:
                D[userlist] = [Com.rstrip()]
            else:
                D[userlist].append(Com.rstrip())
            #check if the task is overdue
            for i in dates2:
                    print(i.split(" "))
                    if int(i.split(" ")[2]) >= currentyear:
                        overdue +=1
                    elif int(i.split(" ")[2])< currentyear:
                        if datesd[i.split(" ")[1]] > currentmonth and int(i.split(" ")[0])> currentday:
                            overdue +=1
                    else:
                        overdue = 0
        
                
            
                        
        with open("tasks.txt","r") as f:
            for line in f:
                line.rstrip()
                data = line.split(", ")[4]
                userlist = line.split(", ")[0]
                if userlist not in datess:
                    datess[userlist] = [data] + [overdue]
                else:
                    datess[userlist].append(data)
                    datess[userlist].append(overdue)
            
        #loop through the keys in the dictionarys to loop through each value
        for keys in tasks:
            c = len(tasks[keys])
            entry += "\n" +keys +' = '+ str(c)
            numtask +="\n"+ keys +' = ' + str(((c)/line_count)*100)+'%'
        for keys in D:
            T = D[keys].count("Yes")
            I = D[keys].count("No")
            amount = len(D[keys])
            numcomp += "\n" + keys + ' = ' +str((T/amount)*100)
            numinc += "\n" + keys + ' = ' + str((I/amount)*100)
            
      
       
    #open in write mode to generate a new text file
    with open("user_overview.txt","w") as u:
        u.write("The total number of users: {} ".format(len(user)))
        u.write("\n")
        u.write("The total number of tasks per user is as follows: ")
        u.write("\n")
        u.write(entry)
        u.write("\n")
        u.write("The percentage of the total number of tasks completed by each user is as follows: ")
        u.write("\n")
        u.write(numtask)
        u.write("\n")
        u.write("The percentage of the total number of tasks assigned to each user that has been completed: ")
        u.write(numcomp)
        u.write("\n")
        u.write("The percentage of the total number of tasks assigned to each user that must still be completed: ")
        u.write("\n")
        u.write(numinc)
    #open again in read mode to display on screen
    with open("user_overview.txt", "r") as u:
        for line in u:
            print(line)

            
        
             
                                      
#define stats()
def stats():
    count = 0
    with open("tasks.txt","r") as task:
        for line in task:
            line = line.split(',')
            count +=1
        print("{0:30}{1}".format("The total number of users are:          ", len(user)))
        print("{0:10}{1}".format("The total number of assigned tasks are: \n", count))

    

    

#open file in read mode
with open("user.txt", "r") as f:
    #readlines in the file and strip the new line character
    for line in f:
        details.append(line.rstrip())
    #split the lines and append them to a list
    for element in details:
        element = element.split(', ')
        #remove the empty space
        for i in element:
            i.split()
            if i != '':
                users.append(i)
    #split the list into two seperate lists for passwords and usernames
    for i in range(0,len(users)):
        if i == 0:
            user.append(users[0])
        elif i == 1:
            passwords.append(users[1])
        elif i %2 == 0:
            user.append(users[i])
        else:
            passwords.append(users[i])

            
                
#set the variable to False initially       
validcredentials = False

#create a while loop that prompts the user for input while validcredentials = False
while (not validcredentials):
    
    username = input("Please enter your username: \n")
    password = input("please enter your password: \n")
    #index the list of usernames and passwords and check if the set of inputted usernames and passwords are in the list at the same position in each respective list
    for i in range(0,len(user)):
        if (username == user[i] and password == passwords[i]):
            validcredentials = True
    #check if password and usernames are both correct, or one is correct or neither
    if password in passwords and username  not in user:
        print("invalid username")
    if username in user and password not in passwords:
        print("invalid password")
    if username not in user and password not in passwords:
        print("invalid credentials")
    
        
#if True, then display menu       
while validcredentials:
    #if logged in as admin, display a different menu
    if username == "admin":
        print("\n Please select one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\nds - display statistics\ne - exit")
    else:
        print("\n Please select one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ne - exit")

    choice = input()
    #create loops for each choice in the menu
    if choice == "e":
        break
        
    if choice == "r":
        if username == "admin":
            reg_user()                         
        else:
            print("You do not have authorization for this. Please log in as admin")

    if choice == "a":
        add_task()

    if choice == 'va':
        view_all()

    if choice == 'vm':
        view_mine()
        
    if choice == 'gr' and username == "admin":
        gen_rep()
        
    #check if logged in as admin AND the choice is "s"                
    if username == "admin" and choice == "s":
        stats()
        
                
            
        
    
          
