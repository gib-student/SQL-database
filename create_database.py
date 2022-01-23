"""
Sprint 1 - Trevor Gibb

This simple database will store names, contract value,
age, and sex for customers.
"""

import sqlite3

# Connect to the database
connection = sqlite3.connect('records.db')
cursor = connection.cursor()

# Create table (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS customers (name TEXT, cv REAL, address TEXT, age REAL, sex TEXT)")

def get_name(cursor):
    cursor.execute("SELECT name FROM customers")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No names in database")
        return None
    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
    choice = 0
    while choice < 1 or choice > len(results):
        choice = int(input("Name ID: "))
    return results[choice-1][0]


choice = None
while choice != "7":
    print("1) Display Customers")
    print("2) Add Customer")
    print("3) Update Customer Contract Value")
    print("4) Update Customer Address")
    print("5) Update Customer Age")
    print("6) Delete Customer")
    print("7) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display Customers
        cursor.execute("SELECT * FROM customers ORDER BY cv DESC")
        print("{:>10}  {:>10}  {:>25}  {:>15}  {:>10}".format("Name", "CV", "Address", "Age", "Sex"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>25}  {:>15}  {:>10}".format(record[0], record[1], record[2], record[3], record[4]))
    elif choice == "2":
        # Add New Customer
        try:
            name = input("Name: ")
            cv = input("Contract Value: ")
            address = input("Address: ")
            age = float(input("Age: "))
            sex = input("Sex: ")
            values = (name, cv, address, age, sex)
            cursor.execute("INSERT INTO customers VALUES (?,?,?,?,?)", values)
            connection.commit()
        except ValueError:
            print("Invalid contract value!")
    elif choice == "3":
        # Update Customer contract value
        try:
            name = input("Name: ")
            cv = float(input("Contract Value: "))
            values = (cv, name) # Make sure order is correct
            cursor.execute("UPDATE customers SET cv = ? WHERE name = ?", values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid name!")
        except ValueError:
            print("Invalid contract value!")
    elif choice == "4":
        # Change customer address
        name = input("Name: ")
        address = input("Address: ")
        values = (address, name)
        cursor.execute("UPDATE customers SET address = ? WHERE name = ?", values)
        connection.commit()
        if cursor.rowcount == 0:
            print("Invalid Name!")
    elif choice == "5":
        # Change customer age
        try:
            name = input("Name: ")
            age = float(input("Age:  "))
            values = (age, name)
            cursor.execute("UPDATE customers SET age = ? WHERE name = ?", values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid name!")
        except ValueError:
            print("Invalid age!")
    elif choice == "6":
        # Delete employee
        name = get_name(cursor)
        if name == None:
            continue
        values = (name, )
        cursor.execute("DELETE FROM customers WHERE name = ?", values)
        connection.commit()
    print()

# Close the database connection before exiting
connection.close()