import lisst
import dateandtime
def returnBook():
    print("Please note that you need to return all book at once\nYou can't return books multiple times\n")
    name=input("Enter the first name of borrower: ")
    borrower="Borrow-"+name+".txt"
    try:
        with open(borrower,"r") as newfile:
            lines=newfile.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(borrower,"r") as newfile:
            data=newfile.read()
            print(data)
    except:
        print("The borrower name is incorrect\n")
        returnBook()

    returner="Return-"+name+".txt"
    with open(returner,"w+")as newfile:
        newfile.write("                Library Management System \n")
        newfile.write("                   Returned By: "+ name+"\n")
        newfile.write("    Date: " + dateandtime.getDate()+"    Time:"+ dateandtime.getTime()+"\n\n")
        newfile.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(3):
        if lisst.bookname[i] in data:
            with open(returner,"a") as newfile:
                newfile.write(str(i+1)+"\t\t"+lisst.bookname[i]+"\t\t$"+lisst.cost[i]+"\n")
                lisst.quantity[i]=int(lisst.quantity[i])+1
            total+=float(lisst.cost[i])
            
    print("\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        day=int(input("By how many days was the book returned late: "))
        fine=2*day
        with open(returner,"a")as newfile:
            newfile.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total: "+ "$"+str(total))
    with open(returner,"a")as newfile:
        newfile.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("Stock.txt","w+") as newfile:
            for i in range(3):
                newfile.write(lisst.bookname[i]+","+lisst.authorname[i]+","+str(lisst.quantity[i])+","+"$"+lisst.cost[i]+"\n")
