from typing import List

# def list_avg(sequence: List)->float:
#      return sum(sequence) / len(sequence)
 
# list_avg(123)
class Book:
    Types = ("handcover","paperback")
    def __init__(self,name: str, book_type:str, weight: int) -> None:
        self.name=name
        self.book_type= book_type
        self.weight=weight
        
    def __repr__(self) -> str:
        return f"Book {self.name}, {self.book_type}, weighing {self.weight} "
    
    @classmethod
    def handcover(cls, name: str, page_weight: int)->"Book":
        return cls(name,cls.Types[0], page_weight +200)
    
    @classmethod
    def paperback(cls, name:str, page_weight: int)-> "Book":
        return cls(name, cls.Types[1], page_weight*3)
    

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books