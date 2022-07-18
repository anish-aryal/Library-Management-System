import dateandtime
import lisst

def borrowBook():
    borrow=False
    while(True):
        firstname=input("First Name: ")
        if firstname.isalpha():
            break
        print("Only Alphabets without any spacing are valid"'\n')
    while(True):
        lastname=input("Last Name: ")
        if lastname.isalpha():
            break
        print("Only Alphabets without any spacing are valid"'\n')
            
    borrower="Borrow-"+firstname+".txt"
    with open(borrower,"w+") as newfile:
        newfile.write("               Islington Library Borrowers \n")
        newfile.write("    Borrowed By: "+ firstname+" "+lastname+"\n")
        newfile.write("    Date: " + dateandtime.getDate()+"    Time:"+ dateandtime.getTime()+"\n\n")
        newfile.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    while borrow==False:
        print('\n'"Enter respective number for respective books"'\n')
        for i in range(len(lisst.bookname)):
            print("Enter", i, "for borrowing", lisst.bookname[i])
        try:
            print('\n')   
            bookno=int(input("Enter the book number of the book you want to borrow: "))
            if bookno<0:
                print("input cannot be negative")
            else:    
                lisst.quantity[bookno]=int(lisst.quantity[bookno])
                try:

                    if(lisst.quantity[bookno])>0:
                        print("Book is borrowed sucessfully \n")
                        with open(borrower,"a") as newfile:
                            newfile.write("1. \t\t"+ lisst.bookname[bookno]+"\t\t  "+lisst.authorname[bookno]+"\n")

                        lisst.quantity[bookno]=lisst.quantity[bookno]-1
                        with open("Stock.txt","w+") as newfile:
                            for i in range(3):
                                newfile.write(lisst.bookname[i]+","+lisst.authorname[i]+","+str(lisst.quantity[i])+","+"$"+lisst.cost[i]+"\n")


                    loop=True
                    snnumber=1
                    while loop==True:
                        choice=str(input("Enter 'Y' to borrow more books and 'N' to exit borrow process: "))
                        if(choice.upper()=="Y"):
                            snnumber=snnumber+1
                            print("\nPlease select from options above ")
                            
                            bookindex=int(input("Enter book number for next book: "))
                            with open(borrower,"r") as newfile:
                                if (lisst.bookname[bookindex] in newfile.read()):
                                    print("Book already borrowed '\n'You can't borrow same book twice!!!!!!!!!!!'\n'Please select another book. ")
                                else: 
                                    if(int(lisst.quantity[bookindex])>0):
                                        print("Book is borrowed sucessfully\n")
                                        with open(borrower,"a") as newfile:
                                            newfile.write(str(snnumber) +". \t\t"+ lisst.bookname[bookindex]+"\t\t  "+lisst.authorname[bookindex]+"\n")
                                        lisst.quantity[bookindex]=int(lisst.quantity[bookindex])-1
                                        with open("Stock.txt","w+") as newfile:
                                            for i in range(3):
                                                newfile.write(lisst.bookname[i]+","+lisst.authorname[i]+","+str(lisst.quantity[i])+","+"$"+lisst.cost[i]+"\n")
                                                borrow=False
                                    else:
                                        loop=False
                                        break
                        elif (choice.upper()=="N"):
                            print ("\nThank you Borrowing books form us.\n Happy Reading!! ")
                            print("------------------------------------------------------")
                            borrow=True
                            loop=False
                            break
                        else:
                            print("Please enter the valid number from the list")
                        
                    else:
                        print("Book is out of stock")
                        borrowBook()
                        borrow=False
                except:
                    print("Enter the valid value")  
        except:
            print("Please enter the valid book number.")
            print("------------------------------------")
