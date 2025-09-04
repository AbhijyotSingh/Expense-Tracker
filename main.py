import csv

def add_expense(n): #Adds new expense
    with open(filename,"a+") as file:
        writer=csv.writer(file)
        for i in range(1,n+1):
            print(f"For {i} expense(s)")
            try:
                date=input("Enter date (DD-MM-YYYY):")
                des=input("Enter the description:")
                expense=int(input("Enter the amount:"))
            except ValueError:
                print("Only integral values allowed.")
            else:
                lis=[date,des,expense]
                writer.writerow(lis)
        file.close()
            
def update_expense():#Updates previously stored expense, has some issues - minor data loss
    main_lis=[]
    sec_lis=[]
    with open(filename,"r",newline="") as file:
        reader=csv.reader(file)
        for i in reader:
            if i==[]:
                continue
            else:
                print(i)
                ans=input("Is this your file (yes/no):")
                if ans.lower()=="no":
                    main_lis.append(i)
                elif ans.lower()=="yes":
                    ques=input("What do you want to update (expense/description):")
                    with open(filename,"w") as file1:
                        writer=csv.writer(file1)
                        if ques.lower()=="expense":
                                try:
                                    new_exp=int(input("Enter new expense:"))
                                except ValueError:
                                    print("Only integral values allowed.")
                                else:
                                    i[2]=new_exp
                                    print("Your updated record is:",i)
                                    sec_lis.append(i)
                                    print("Expense updated.")
                        elif ques.lower()=="description":
                                new_des=input("Enter new description:")
                                i[1]=new_des
                                print("Your updated record is:",i)
                                sec_lis.append(i)
                                print("Description updated.")
                        else:
                                print("Only these options are available,")
                else:
                    print("No other options available.")
    with open(filename,"a+") as file2:
        writer=csv.writer(file2)
        for j in main_lis:
            writer.writerow(j)
        for i in sec_lis:
                writer.writerow(i)
  
def view_all(): #Shows all expenses
    with open(filename,"r") as file:
        reader=csv.reader(file)
        print("All the records are as follows.")
        for i in reader:
            if i==[]:
                pass
            else:
                print(i)
     
def delete(): #Deletes expenses through itration
    main_lis=[]
    with open(filename,"r") as file:
        reader=csv.reader(file)
        for i in reader:
            if i==[]:
                pass
            else:
                print(i)         
                ques=input("Do you want to delete this file (yes/no):")
                if ques.lower()=="no":
                    main_lis.append(i)
                elif ques.lower()=="yes":
                    with open(filename,"w") as file1:
                        print("Record deleted.")
                else:
                    print("Only these options are available.")
    with open(filename,"a+") as file2:
        writer=csv.writer(file2)
        for i in main_lis:
            writer.writerow(i)
  
def summary_month(): #Summarises the amount of a purchase in a month of current year
    sum=0
    month=input("Enter the month and year for which you want your summary of expenses for (MM-YYYY):")
    with open(filename,"r") as file:
        reader=csv.reader(file)
        for i in reader:
            if i==[]:
                pass
            else:
                date_ques=i[0]
                if date_ques[3::]==month:
                    amount=int(i[2])
                    sum+=amount
                else:
                    pass
        print(f"Total summary for the month is {sum}")
        
def summary_all(): #Summarises all the amount
    sum=0
    with open(filename,"r") as file:
        reader=csv.reader(file)
        for i in reader:
            if i==[]:
                pass
            else:
                amount=int(i[2])
                sum+=amount
        print(f"The total expenses is:", sum)

def budget_warn(): #Shows warning if the user exceeds budget limit for a month
    sum=0
    month=input("Enter the month and year for which you want your summary of expenses for (MM-YYYY):")
    with open(filename,"r") as file:
        reader=csv.reader(file)
        for i in reader:
            if i==[]:
                pass
            else:
                date_ques=i[0]
                if date_ques[3::]==month:
                    amount=int(i[2])
                    sum+=amount
                else:
                    pass
        print(f"Total summary for the month is {sum}")
        try:
            budget=int(input("Set budget:"))
        except ValueError:
            print("Only integral values allowed.")
        else:
            if sum>budget:
                print("Expenses exceed budget.")
            else:
                print("You are fine.")
            
def main(): #Main function
    print("-----Welcome to Expense Tracker-----")
    print("Press 1 to add an expense with a description and amount.")
    print("Press 2 to update an expense.")
    print("Press 3 to see all expenses.")
    print("Press 4 to delete a record.")
    print("Press 5 to see summary of expenses for a particular month of current year.")
    print("Press 6 to see summary of all expenses.")
    print("Press 7 to set a budget for a month of current year.")
    try:
        ans=int(input("Enter your choice:"))
    except ValueError:
        print("Only integral values allowed.")
    else:
        if ans==1:  
            try:
                num=int(input("Enter the number of expenses you want to add:"))
            except ValueError:
                print("Only integral values allowed.")
            else:
                add_expense(num)
        elif ans==2:
            update_expense()
        elif ans==3:
            view_all()
        elif ans==4:
            delete()
        elif ans==5:
            summary_month()
        elif ans==6:
            summary_all()
        elif ans==7:
            budget_warn()
        else:
            print("Only these options are available.")
            
filename="tracker.csv"

if __name__=="__main__":
    main()

