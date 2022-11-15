#import db
from tkinter import *
from tkinter.ttk import *

LARGE_FONT = ("Albertus Medium", 32)

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

        #grid, labels, and buttons to be added
    def add(self, box):
        myLabel = Label(box, text="The value has been added!")
        myLabel.grid(row=4, column=0)

    def delete(self, box):
        myLabel = Label(box, text="The value has been deleted.")
        myLabel.grid(row=4, column=0)

    def display(self, database):
        select_all = database
        return select_all

    def insert(self, database, val1, val2, val3):
        expense = val1.get()
        cost = val2.get()
        date = val3.get()
        inserted = database(expense, cost, date)
        return inserted
    
    def find_expense(self, database, val1, val2):
        expense = val1.get()
        cost = val2.get()
        locate = database(expense, cost)
        return locate
    
    def delete_expense(self, database, val1, val2):
        expense = val1.get()
        cost = val2.get()
        delete = database(expense, cost)
        return delete

    # Builds main window with each expense type
    def main_window(self):
        button1 = Button(self.frame, text="Fixed Expenses", command=self.fixed)
        button1.pack()

        button2 = Button(self.frame, text="Recurring Expenses", command=self.recurring)
        button2.pack()

        button2 = Button(self.frame, text="Non-recurring Expenses", command=self.nonrecurring)
        button2.pack()

        button2 = Button(self.frame, text="Extraneous Expenses", command=self.extraneous)
        button2.pack()








    def fixed(self):
        top = TopLevel(self.frame)

    def recurring(self):
        top = TopLevel(self.frame)

    def nonrecurring(self):
        top = TopLevel(self.frame)

    def extraneous(self):
        top = TopLevel(self.frame)





# The main function
def main():
    #db.create_tables(connection)
    root = Tk()
    root.geometry('250x200')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)

    root.mainloop()

main()