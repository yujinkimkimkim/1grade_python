class Author:
    def __init__(self, name = "yujin", email = "kimyj4852@naver.com", gender = "f"):
        self.__name = name
        self.__email = email
        self.__gender = gender
    def getName(self):
        return self.__name
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email
    def getGender(self):
        return self.__gender
    def print(self):
        print('"{}({})at {}"'.format(self.__name,self.__gender,self.__email))

class Book:
    def __init__(self, name = "yujinkim's book", author = Author(), price = 20.2, qtyInStock = 30):
        self.__name = name
        self.__author = author
        self.__price = price
        self.__qtyInStock = qtyInStock
    def getName(self):
        return self.__name
    def getAuthor(self):
        return self.__author
    def getPrice(self):
        return self.__price
    def setPrice(self, price):
        self.__price = price
    def getQtyInStock(self):
        return self.__qtyInStock
    def setQtyInStock(self, qtyInStock):
        self.__qtyInStock = qtyInStock
    def print(self):
        print(f"책 제목:{self.__name}, 가격 : {self.__price}$, 출판부수 : {self.__qtyInStock}")
        print(f"지은이: {self.__author.getName()}, 지은이 이메일:{self.__author.getEmail()},지은이 성별:{self.__author.getGender()}")
        print(self.__author.print())
    def getAuthorName(self):
        return self.__author.getName()

a = Book()
a.print()