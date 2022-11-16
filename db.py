import sqlite3
import datetime
now = datetime.datetime.utcnow()

CREATE_FIXED = "CREATE TABLE IF NOT EXISTS fixed (id INTEGER PRIMARY KEY,expense TEXT, cost INTEGER, date DATE);"
CREATE_HOUSEHOLD = "CREATE TABLE IF NOT EXISTS household (id INTEGER PRIMARY KEY,expense TEXT, cost INTEGER, date DATE);"
CREATE_ENTERTAINMENT = "CREATE TABLE IF NOT EXISTS entertainment (id INTEGER PRIMARY KEY,expense TEXT, cost INTEGER, date DATE);"
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INTEGER PRIMARY KEY,expense TEXT, cost INTEGER, date DATE);"



INSERT_FIXED = "INSERT INTO fixed (expense, cost, date) VALUES(?,?,?);"
INSERT_HOUSEHOLD = "INSERT INTO household (expense, cost, date) VALUES(?,?,?);"
INSERT_ENTERTAINMENT = "INSERT INTO entertainment (expense, cost, date) VALUES(?,?,?);"
INSERT_OTHER = "INSERT INTO other (expense, cost, date) VALUES(?,?,?);"


SELECT_ALL1 = "SELECT * FROM fixed;"
SELECT_ALL2 = "SELECT * FROM household;"
SELECT_ALL3 = "SELECT * FROM entertainment;"
SELECT_ALL4 = "SELECT * FROM other;"

SELECT_FIXED = "SELECT * FROM fixed WHERE expense = ? AND cost = ?;"
SELECT_HOUSEHOLD = "SELECT * FROM household WHERE expense = ? AND cost = ?;"
SELECT_ENTERTAINMENT = "SELECT * FROM entertainment WHERE expense = ? AND cost = ?;"
SELECT_OTHER = "SELECT * FROM other WHERE expense = ? AND cost = ?;"

DELETE_FIXED = "DELETE FROM fixed WHERE expense = ? AND cost = ?;"
DELETE_HOUSEHOLD = "DELETE FROM household WHERE expense = ? AND cost = ?;"
DELETE_ENTERTAINMENT = "DELETE FROM entertainment WHERE expense = ? AND cost = ?;"
DELETE_OTHER = "DELETE FROM other WHERE expense = ? AND cost = ?;"





###create for every table###
def create_tables():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_OTHER)

###INSERT VALUES###

def insert_fixed(expense, cost, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_FIXED, (expense, cost, date))
        conn.commit()



def insert_household(expense, cost, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_HOUSEHOLD, (expense, cost, date))
        conn.commit()
        c.close()

def insert_entertrainment(expense, cost, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_ENTERTAINMENT, (expense, cost, date))
        conn.commit()
        c.close()

def insert_other(expense, cost, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_OTHER, (expense, cost, date))
        conn.commit()
        c.close()

###SELECT_ALL###



def select_all_fixed():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL1)
        #have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output





def select_all_household():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL2)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_all_entertrainment():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL3)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_all_other():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL4)
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

###SELECT SPECIFIC###

def select_fixed(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_FIXED, (expense, cost))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_household(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_HOUSEHOLD, (expense, cost))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_entertainment(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ENTERTAINMENT, (expense, cost))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_other(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_OTHER, (expense, cost))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


###DELETE VALUE###
def delete_fixed(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_FIXED, (expense, cost))
        conn.commit()
        c.close()

def delete_household(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_HOUSEHOLD, (expense, cost))
        conn.commit()
        c.close()

def delete_entertainment(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ENTERTAINMENT, (expense, cost))
        conn.commit()
        c.close()

def delete_other(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_OTHER, (expense, cost))
        conn.commit()
        c.close()