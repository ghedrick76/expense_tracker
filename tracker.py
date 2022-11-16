import db
from tkinter import *
from tkinter.ttk import *

LARGE_FONT = ("Albertus Medium", 32)

# Creates the ExpenseTracker class
class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

    # Create the add and delete functions for the expense types   
    def add(self, box):
        myLabel = Label(box, text="The value has been added!")
        myLabel.grid(row=4, column=0)

    def delete(self, box):
        myLabel = Label(box, text="The value has been deleted.")
        myLabel.grid(row=4, column=0)

    # Creates the functions to connect to the database
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

    # Builds main window and creates a button for each expense type
    def main_window(self):
        button1 = Button(self.frame, text="Fixed Expenses", command=self.fixed)
        button1.pack()

        button2 = Button(self.frame, text="Recurring Expenses", command=self.recurring)
        button2.pack()

        button3 = Button(self.frame, text="Non-recurring Expenses", command=self.nonrecurring)
        button3.pack()

        button4 = Button(self.frame, text="Extraneous Expenses", command=self.extraneous)
        button4.pack()

        button5 = Button(self.frame, text="Analysis", command=self.analysis)
        button5.pack()

        button6 = Button(self.frame, text="Exit", command=exit)
        button6.pack()
        







    # Creates the Fixed Expense window
    def fixed(self):
        top = Toplevel(self.frame)
        top.title('Fixed Expenses')
        l1 = Label(top, text="Expense Type").grid(row = 1, column = 0, sticky = W, pady = 2)
        l2 = Label(top, text="Cost").grid(row = 2, column = 0, sticky = W, pady = 2)
        l3 = Label(top, text="Date of Expense").grid(row = 3, column = 0, sticky = W, pady = 2)

        # Creates the entry widget
        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        # Creates the text object
        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # Creates the buttons for each action
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_fixed,e1,e2,e3), self.add(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display(db.select_all_fixed()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_fixed, e1,e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_fixed, e1,e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B4 = Button(top, text="Sum", command=lambda: (self.sum_expense(db.sum_fixed, e1,e2), self.sum(top)))
        B4.grid(row=3, column=2)

        B5= Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    # Creates the Recurring Expense window
    def recurring(self):
        top = Toplevel(self.frame)
        top.title('Recurring Expenses')
        l1 = Label(top, text="Expense Type").grid(row = 1, column = 0, sticky = W, pady = 2)
        l2 = Label(top, text="Cost").grid(row = 2, column = 0, sticky = W, pady = 2)
        l3 = Label(top, text="Date of Expense").grid(row = 3, column = 0, sticky = W, pady = 2)

        # Creates the entry widget
        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        # Creates the text object
        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # Creates the buttons for each action
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_recurring,e1,e2,e3), self.add(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display(db.select_all_recurring()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_recurring, e1,e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_recurring, e1,e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B4 = Button(top, text="Sum", command=lambda: (self.sum_expense(db.sum_recurring, e1,e2), self.sum(top)))
        B4.grid(row=3, column=2)

        B5= Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    # Creates the Non-Recurring Expense window
    def nonrecurring(self):
        top = Toplevel(self.frame)
        top.title('Non-Recurring Expenses')
        l1 = Label(top, text="Expense Type").grid(row = 1, column = 0, sticky = W, pady = 2)
        l2 = Label(top, text="Cost").grid(row = 2, column = 0, sticky = W, pady = 2)
        l3 = Label(top, text="Date of Expense").grid(row = 3, column = 0, sticky = W, pady = 2)

        # Creates the entry widget
        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        # Creates the text object
        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # Creates the buttons for each action
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_nonrecurring,e1,e2,e3), self.add(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display(db.select_all_nonrecurring()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_nonrecurring, e1,e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_nonrecurring, e1,e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B4 = Button(top, text="Sum", command=lambda: (self.sum_expense(db.sum_nonrecurring, e1,e2), self.sum(top)))
        B4.grid(row=3, column=2)

        B5= Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    # Creates the Extraneous Expense window
    def extraneous(self):
        top = Toplevel(self.frame)
        top.title('Extraneous Expenses')
        l1 = Label(top, text="Expense Type").grid(row = 1, column = 0, sticky = W, pady = 2)
        l2 = Label(top, text="Cost").grid(row = 2, column = 0, sticky = W, pady = 2)
        l3 = Label(top, text="Date of Expense").grid(row = 3, column = 0, sticky = W, pady = 2)

        # Creates the entry widget
        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        # Creates the text object
        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # Creates the buttons for each action
        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_extraneous,e1,e2,e3), self.add(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, END), text.insert(END, self.display(db.select_all_extraneous()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(1.0, END), text.insert(END, self.find_expense(db.select_extraneous, e1,e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_extraneous, e1,e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B4 = Button(top, text="Sum", command=lambda: (self.sum_expense(db.sum_extraneous, e1,e2), self.sum(top)))
        B4.grid(row=3, column=2)

        B5= Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    # Creates the Analysis window (in progress)
    def analysis(self):
        top = Toplevel(self.frame)





# The main function
def main():
    #db.create_tables(connection)
    root = Tk()
    root.geometry('250x200')
    root.title("Expense Tracker")
    tracker = ExpenseTracker(root)

    root.mainloop()

# Runs the main function
main()