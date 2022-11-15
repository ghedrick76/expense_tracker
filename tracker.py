import db
from tkinter import *
from tkinter.ttk import *

LARGE_FONT = ("Albertus Medium", 32)

class ExpenseTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

        #grid, labels, and buttons to be added

# The main function to be added at the end of the script
def main():
    #db.create_tables(connection)
    root = Tk()
    root.gemoetry('250x200')
    root.title("Expense Tracking Application")
    tracker = ExpenseTracker(root)

    root.mainloop()

main()