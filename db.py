import sqlite3
import datetime
now = datetime.datetime.utcnow()

CREATE_FIXED = "CREATE TABLE IF NOT EXISTS fixed (id INTEGER PRIMARY KEY,expense TEXT, cost INTEGER, date DATE);"
CREATE_RECURRING = "CREATE TABLE IF NOT EXISTS recurring (id INTEGER PRIMARY KEY,expense TEXT, cost INTEGER, date DATE);"
CREATE_NONRECURRING = "CREATE TABLE IF NOT EXISTS nonrecurring (id INTEGER PRIMARY KEY,expense TEXT, cost INTEGER, date DATE);"
CREATE_EXTRANEOUS = "CREATE TABLE IF NOT EXISTS extraneous (id INTEGER PRIMARY KEY,expense TEXT, cost INTEGER, date DATE);"

SUM_FIXED = "SELECT SUM(cost) FROM fixed;"
#SUM_FIXED = "SUM fixed (cost) VALUES(?);"

INSERT_FIXED = "INSERT INTO fixed (expense, cost, date) VALUES(?,?,?);"
INSERT_RECURRING = "INSERT INTO recurring (expense, cost, date) VALUES(?,?,?);"
INSERT_NONRECURRING = "INSERT INTO nonrecurring (expense, cost, date) VALUES(?,?,?);"
INSERT_EXTRANEOUS = "INSERT INTO extraneous (expense, cost, date) VALUES(?,?,?);"


SELECT_ALL1 = "SELECT * FROM fixed;"
SELECT_ALL2 = "SELECT * FROM recurring;"
SELECT_ALL3 = "SELECT * FROM nonrecurring;"
SELECT_ALL4 = "SELECT * FROM extraneous;"

SELECT_FIXED = "SELECT * FROM fixed WHERE expense = ? AND cost = ?;"
SELECT_RECURRING = "SELECT * FROM recurring WHERE expense = ? AND cost = ?;"
SELECT_NONRECURRING = "SELECT * FROM nonrecurring WHERE expense = ? AND cost = ?;"
SELECT_EXTRANEOUS = "SELECT * FROM extraneous WHERE expense = ? AND cost = ?;"

DELETE_FIXED = "DELETE FROM fixed WHERE expense = ? AND cost = ?;"
DELETE_RECURRING = "DELETE FROM recurring WHERE expense = ? AND cost = ?;"
DELETE_NONRECURRING = "DELETE FROM nonrecurring WHERE expense = ? AND cost = ?;"
DELETE_EXTRANEOUS = "DELETE FROM extraneous WHERE expense = ? AND cost = ?;"





###create for every table###
def create_tables():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_EXTRANEOUS)

create_tables()

# SUM VALUES

# def sum_fixed(cost):
#     conn = sqlite3.connect('data.db')
#     with conn:
#         c = conn.cursor()
#         c.execute(SUM_FIXED, (cost))
#         conn.commit()




        
def sum_fixed(cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SUM_FIXED, cost)
        #have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = 'The total sum of expenses is $'
        for x in list:
            output = output + str(x[0]) + '\n'
        return output

###INSERT VALUES###

def insert_fixed(expense, cost, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_FIXED, (expense, cost, date))
        conn.commit()



def insert_recurring(expense, cost, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_RECURRING, (expense, cost, date))
        conn.commit()
        c.close()

def insert_entertainment(expense, cost, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_NONRECURRING, (expense, cost, date))
        conn.commit()
        c.close()

def insert_extraneous(expense, cost, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_EXTRANEOUS, (expense, cost, date))
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





def select_all_recurring():
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

def select_all_extraneous():
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

def select_recurring(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_RECURRING, (expense, cost))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_nonrecurring(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_NONRECURRING, (expense, cost))
        # have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_extraneous(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_EXTRANEOUS, (expense, cost))
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

def delete_recurring(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_RECURRING, (expense, cost))
        conn.commit()
        c.close()

def delete_nonrecurring(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_NONRECURRING, (expense, cost))
        conn.commit()
        c.close()

def delete_extraneous(expense, cost):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_EXTRANEOUS, (expense, cost))
        conn.commit()
        c.close()