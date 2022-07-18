import Return
import lisst
import dateandtime
import borrow
import lisst
import Return


def librarymanagement():
    print("          Welcome to Islington Library        ","\n",
              "-------------------------------------------------------------------------",'\n')
    print("Library Mangaement System Program Guide",'\n',
              "---------------------------------------",'\n')

    while(True):
        
        print("--------------------------------------------------------------------------","\n",
              "Enter 1 to view all the available books","\n",
              "Enter 2 to borrow books form the library","\n",
              "Enter 3 to return the borrowed books","\n",
              "Enter 4 to exit the program","\n",)
        try:
            entered=int(input("Enter a number for a task you want to do: "))
            print('\n')
            if(entered==1):
                print("Books Available to borrow",'\n')
                file= open("stock.txt","r")
                lines=file.read()
                print(lines)
            elif(entered==2):
                lisst.booklist()
                borrow.borrowBook()
            elif(entered==3):
                lisst.booklist()
                Return.returnBook()
            elif(entered==4):
                print('Thank you for visiting "Islington Library."')
                break
            else:
                print("Please enter a valid number")
                 
        except:
            
            print('\n'+"Invalid input!!! \nPlease enter the valid value"+'\n')

librarymanagement()
