#!/usr/bin/env python
# coding: utf-8

# 1. What is the primary goal of Object-Oriented Programming (OOP)?
# 
OOP- Object Oriented Programming uses the classes and object. To create the reusable code. 
# 2. What is an object in Python?
Object is dervied from the class . Object is created using class.Object is the replica of the class.It is the blueprint copy of the Class
# 3. What is a class in Python?
Class is the blueprint . Which has attributes , constructors and methods
# 4. What are attributes and methods in a class?
Attributes are the variables defined in the class . Methods are the functions used in the class. It doesn't represent the properties of the class.

# 5. What is the difference between class variables and instance variables in Python?
Class Variables are the variables defined inside the class. class variables are shared with all the instance in the class .

Instance variables are variable shared to only current using instance.
# 6. What is the purpose of the self parameter in Python class methods?
Self is the keyword used in the methods.It refers the current instance of the class
# 7. For a library management system, you have to design the "Book" class with OOP
# principles in mind. The “Book” class will have following attributes:
# a. title: Represents the title of the book.
# b. author: Represents the author(s) of the book.
# c. isbn: Represents the ISBN (International Standard Book Number) of the book.
# d. publication_year: Represents the year of publication of the book.
# e. available_copies: Represents the number of copies available for checkout.
# The class will also include the following methods:
# a. check_out(self): Decrements the available copies by one if there are copies
# available for checkout.
# b. return_book(self): Increments the available copies by one when a book is
# returned.
# c. display_book_info(self): Displays the information about the book, including its
# attributes and the number of available copies.

# In[1]:


class Book:
    #constructors
    def __init__(self,title,author,isbn,publication_year,available_copies):
        #attributes
        self.title=title
        self.author=author
        self.isbn=isbn
        self.publication_year=publication_year
        self.available_copies=available_copies
      #method check_out  
    
    def check_out(self):
        if self.available_copies > 0:
            self.available_copies=self.available_copies-1
            print("Check out")
        else:
            print("No books available")
        
        #method
    def return_book(self):
        self.available_copies=self.available_copies+1
        print("Return Book")
       
    #mehod
    def display_book_info(self):
        print(f"Title:{self.title}")
        print("Author:",self.author)
        print("International Standard Book Number:",self.isbn)
        print("Publication year:",self.publication_year)
        print("Available copies",self.available_copies)
#object        
book=Book("Myfault","Mercedes Ron",524,2021,56)
book.check_out()
book.display_book_info()
book.return_book()
book.display_book_info()
        


# 8. For a ticket booking system, you have to design the "Ticket" class with OOP
# principles in mind. The “Ticket” class should have the following attributes:
# a. ticket_id: Represents the unique identifier for the ticket.
# b. event_name: Represents the name of the event.
# c. event_date: Represents the date of the event.
# d. venue: Represents the venue of the event.
# e. seat_number: Represents the seat number associated with the ticket.
# f. price: Represents the price of the ticket.
# g. is_reserved: Represents the reservation status of the ticket.
# The class also includes the following methods:
# a. reserve_ticket(self): Marks the ticket as reserved if it is not already reserved.
# b. cancel_reservation(self): Cancels the reservation of the ticket if it is already
# reserved.
# c. display_ticket_info(self): Displays the information about the ticket, including its
# attributes and reservation status.
# 

# In[7]:


class Ticket:
    def __init__(self,ticket_id,event_name,event_date,venue,price,is_reserved):
        self.ticket_id=ticket_id
        self.event_name=event_name
        self.event_date=event_date
        self.venue=venue
        self.price=price
        self.is_reserved=is_reserved
    
    def reserve_ticket(self):
        self.is_reserved.lower()
        if self.is_reserved != 'reserved':
            self.is_reserved='reserved'
            
        else :
            print("Ticket is already reserved")
            
    def cancel_reservation(self):
        self.is_reserved.lower()
        if self.is_reserved == 'reserved':
            print("Ticket is cancled")
            self.is_reserved='cancled'
        else:
            print("Ticket is not booked")
        
    def display_ticket_info(self):
        print("Ticket id:",self.ticket_id)
        print("Event name:",self.event_name)
        print("Event date:",self.event_date)
        print("Venu:",self.venue)
        print("Price:",self.price)
        print("Reserved status:",self.is_reserved)

ticket=Ticket(45678,"Orange","10-09-2023","HYD",650,"NA")
ticket.reserve_ticket()
ticket.display_ticket_info()

        


# 9. You are creating a shopping cart for an e-commerce website. Using OOP to model
# the "ShoppingCart" functionality the class should contain following attributes and
# methods:
# a. items: Represents the list of items in the shopping cart.
# The class also includes the following methods:
# 
# a. add_item(self, item): Adds an item to the shopping cart by appending it to the
# list of items.
# b. remove_item(self, item): Removes an item from the shopping cart if it exists in
# the list.
# c. view_cart(self): Displays the items currently present in the shopping cart.
# d. clear_cart(self): Clears all items from the shopping cart by reassigning an
# empty list to the items attribute.
# 

# In[11]:


class ShoppingCart:
    def __init__(self,name):
        self.name=name
        self.items=[]
    def add_items(self,items):
        self.items.append(items)
        
    def remove_items(self,items):
        if items in self.items:
            self.items.remove(items)
        else:
            print("ITEM NOT FOUND")
        
    def view_cart(self):
        print(f"Name:{self.name}")
        for items in self.items:
            print(items)
    
    def clear_cart(self):
        self.items.clear()
        print("cleared the list")

shopping=ShoppingCart("Filpkart")
shopping.add_items("ball")
shopping.view_cart()
shopping.clear_cart()


# 10. Imagine a school management system. You have to design the "Student" class using
# OOP concepts.The “Student” class has the following attributes:
# a. name: Represents the name of the student.
# b. age: Represents the age of the student.
# c. grade: Represents the grade or class of the student.
# d. student_id: Represents the unique identifier for the student.
# e. attendance: Represents the attendance record of the student.
# The class should also include the following methods:
# a. update_attendance(self, date, status): Updates the attendance record of the
# student for a given date with the provided status (e.g., present or absent).
# b. get_attendance(self): Returns the attendance record of the student.
# c. get_average_attendance(self): Calculates and returns the average
# attendance percentage of the student based on their attendance record.

# In[2]:


class Student:
    def __init__(self,name,age,grade,student_id,attendance):
        self.name=name
        self.age=age
        self.grade=grade
        self.student_id=student_id
        self.attendance=attendance

    def update_attendance(self,date,status):
        if status=='present':
            self.attendance=self.attendance+1
        else:
            print(f"The student is absent for {self.date}")
        
    def get_attendance(self):
        print("Student Name:",self.name)
        print("Age:",self.age)
        print("Grade:",self.grade)
        print("Student ID:",self.student_id)
        print("Attendance:",self.attendance)
        
    def get_average_attendance(self):
        print("Average of student:",(self.attendance/30))
        
student=Student("Varu",12,"A",5634,18)
student.update_attendance("09-08-2023","present")
student.get_attendance()
student.get_average_attendance()
        
        


# In[ ]:




