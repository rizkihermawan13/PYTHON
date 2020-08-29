class Book:
    def __init__(self,bookId,bookName,bookTechnology,bookPrice,authorname):
        self.bookId=bookId
        self.bookName=bookName
        self.bookTechnology=bookTechnology
        self.bookPrice=bookPrice
        self.authorname=authorname
class BookStore:
    def __init__(self,d,e):
        self.d=d
        self.e=e
    def searchByName(self,a):
        l=[]
        for i,j in self.d.items():
            if j.bookName==a:
                l.append(j)
        return l
    def calculatePriceByTechnology(self,b):
        k=0
        for i,j in self.d.items():
            if j.bookTechnology==b:
                k=k+j.bookPrice
        k=k*0.9
        return k
count=int(input())
d={}
for q in range(count):
    bookId=int(input())
    bookName=input()
    bookTechnology=input()
    bookPrice=int(input())
    authorname=input()
    B=Book(bookId,bookName,bookTechnology,bookPrice,authorname)
    d[bookId]=B
BS=BookStore(d,'Janakiram store')
a=input()
b=input()
c=BS.searchByName(a)
d=BS.calculatePriceByTechnology(b)
if len(c)==0:
    print("No Book Exists with the BookName")
else:
    for i in c:
        print(i.bookId)
        print(i.bookName)
        print(i.bookTechnology)
        print(i.bookPrice)
        print(i.authorname)
if d==0:
    print("0.0")
else:
    print(d)
