# class Student:
#     def __init__(self):
#         self.name = "Daniel"
#         self.grades = (98,78,88,99,95,78)
        
#     def average(self):
#         return sum(self.grades)/ len(self.grades)
        
        

# student = Student()
# print(student.name)
# print(student.grades)
# print(student.average())


# class Student:
#     def __init__(self,name,grades):
#         self.name = name
#         self.grades = grades
        
#     def average(self):
#         return sum(self.grades)/ len(self.grades)
        
        

# student = Student("Tenkorang Daniel",(98,78,88,99,95,78))
# student1 = Student("Nana Sarfo",(98,88,68,59,85,78))
# student2 = Student("Newton Isaac",(98,78,88,99,95,78))
# print(student.name)
# print(student.grades)
# print(student.average())

# print(student1.name)
# print(student1.grades)
# print(student1.average())

# print(student2.name)
# print(student2.grades)
# print(student2.average())



# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def __str__(self) -> str:
#         return f"{self.name}, {self.age} "
    
#     def __repr__(self) -> str:
#         return f"Person {self.name} {self.age}"
    
# dexoangle = Person("Tenkorang Kyei, Daniel",24)
# print(dexoangle)


# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance method of {self} ")
    
#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls} ")
    
#     @staticmethod
#     def static_method():
#         print("Called static method")
        
# test = ClassTest()
# test.instance_method()
# test.class_method()
# test.static_method()

# class Book:
#     Types=("handcover","paperback")
    
#     def __init__(self,name,book_type,weight) -> None:
#         self.name=name
#         self.book_type=book_type
#         self.weight=weight
        
#     def __repr__(self) -> str:
#         return f"{self.name}, {self.book_type}, weighing {self.weight} "
    
#     @classmethod
#     def handcover(cls, name, page_weight):
#         return Book(name,Book.Types[0],page_weight +100)
    
#     @classmethod
#     def paperback(cls,name, page_weight):
#         return Book(name,Book.Types[1],page_weight *5)

# hand_book=Book.handcover("Harry Potter",1500) 
# print(hand_book)  
# paper_book=Book.paperback("Spider Man", 342)
# print(paper_book)
# book = Book("Movies","handcover",230)  
# print(book)    

# class Device:
#     def __init__(self,name,connected_by) -> None:
#         self.name=name
#         self.connected_by=connected_by
#         self.connected=True
        
#     def __str__(self) -> str:
#         return f"Device: {self.name!r} ({self.connected_by}) "
    
#     def disconnect(self):
#         self.connected = False
#         print("Device disconnected")
        

# class Joystick(Device):
#     def __init__(self, name, connected_by,capacity) -> None:
#        super().__init__(name, connected_by)
#        self.capcity= capacity
#        self.remaining_pages=capacity
       
#     def __str__(self) -> str:
#         return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
#     def game(self,pages):
#         if not self.connected:
#             print("Your joystick is not connected")
#             return
#         else:
#             print(f"Printing {pages} pages ")
#             self.remaining_pages =pages
            

# joysticks = Joystick("Ucom Joystick","USB",700)
# joysticks.game(50)
# joysticks.disconnect()
# print(joysticks)
            
            
class BookShelf:
    def __init__(self,*books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} "
    

class Book():
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return f"Book {self.name} "
        
book= Book("King Solomon Mines")
book1= Book("Golang Microservices 101")
book3= Book("The god's of Egypt")
shelf = BookShelf(book,book1,book3)
print(shelf)