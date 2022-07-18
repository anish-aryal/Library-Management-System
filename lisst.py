def booklist():
    global bookname
    global authorname
    global quantity
    global cost
    global books
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    books=[]
    file= open("stock.txt","r")
    lines=file.readlines()
    for line in lines:
        books.append(line.strip('\n'))
    for i in range(len(books)):
        indexno=0
        for a in books[i].split(','):
            if(indexno==0):
                bookname.append(a)
            elif(indexno==1):
                authorname.append(a)
            elif(indexno==2):
                quantity.append(a)
            elif(indexno==3):
                cost.append(a.strip("$"))
            indexno+=1
        
