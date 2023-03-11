import psycopg2
import re
import os
import psycopg2
import re
import os

dbUser = 'postgres'
dbName = 'dblab'
dbPassword = '123'

connection = psycopg2.connect(
    host="127.0.0.1",
    database=dbName,
    user=dbUser,
    password=dbPassword,
    )

EREGEX = r"[^@]+@[^@]+\.[^@]+"
PASSREGEX = r"(?=.?[A-Z])(?=.?[a-z])(?=.?[0-9])(?=.?[#?!@$%^&*-]).{8,}$"


def validationEmail():
    while True:
        email = input("Enter Your Email  : ").lower()
        if re.match(EREGEX, email):
            return email
        else:
            print("Invalid email format.")


def validationPassword():
    while True:
        password = input("Enter Your Password : ")

        if re.match(PASSREGEX, password) and len(password) >= 8:
            return password
        else:
            print("Invalid Password format. and must be greater or equal 8")


def projecttitle(title):
    while True:
        if title.isalpha():
            return title
        else:
            print(f"{title} must consist only of String. Please try again.")


def totalTarget(targetAmount):
    while True:
        if targetAmount.isdigit():
            return targetAmount
        else:
            print(f"{targetAmount} must consist only of numbers. Please try again.")

def Menu(id):
    title = input("Enter your project title : ")
    while title =="":
            title = input("Enter your project title : ")
    protitle = projecttitle(title)
    details = input("Enter your project details : ")
    target = input("Enter Your target : ")
    while target =="" or  target.isalpha():
            target = input("Enter Your target : ")
    dbCursor = connection.cursor()
    sql = "INSERT INTO details (title, details, target,userid) VALUES (%s, %s,%s,%s);"
    data = (protitle, details, target,id)
    dbCursor.execute(sql, data)
    connection.commit()
    dbCursor.close()

def Login():
    email = validationEmail()
    password = validationPassword()
    dbCursor = connection.cursor()
    sql = "SELECT * FROM users WHERE email=%s AND password=%s"
    dbCursor.execute(sql, (email, password))
    user = dbCursor.fetchone()
    print(user)
    if user is None:
        print("Invalid email or password")
    else:
        os.system("clear")
        print("Welcome")
        options(user[0])

    connection.commit()
    dbCursor.close()

    
def showProject(id):
    dbCursor = connection.cursor()
    sql = f"SELECT * FROM details WHERE userid ={id}"
    dbCursor.execute(sql)
    rows = dbCursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()
    dbCursor.close()



def mainOptions():
    while True:
        print("Main Menu:")
        print("1. Registeration ")
        print("2. Login ")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # import registeration
            pass
        elif choice == "2":
            Login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def editContent(id):
    try:
        dbCursor = connection.cursor()
        identifier = input("Enter Your Title do you need to update it :")
        updateQuery = "UPDATE details SET title = %s, details = %s ,target = %s WHERE id = %s AND userid = %s"
        title = input("Enter your project title : ")
        while title =="":
                title = input("Enter your project title : ")
        protitle = projecttitle(title)
        details = input("Enter your project details : ")
        target = input("Enter Your target : ")

        dbCursor.execute(updateQuery, (protitle, details,target, identifier,id))
        connection.commit()
        dbCursor.close()
    except (Exception,psycopg2.Error) as err:
        print(f"{err}try again")



def addContent(id):
    
    title = input("Enter your project title : ")
    while title =="":
        title = input("Enter your project title : ")
    protitle = projecttitle(title)
    details = input("Enter your project details : ")
    target = input("Enter Your target : ")
    while target =="" or  target.isalpha():
        target = input("Enter Your target : ")
    totlaltarget = totalTarget(target)
    try:
        dbCursor = connection.cursor()
        sql = "INSERT INTO details (title, details, target,userid) VALUES (%s, %s,%s,%s);"
        data = (protitle, details, totlaltarget,id)
        dbCursor.execute(sql, data)
        connection.commit()
        dbCursor.close()
    except (Exception,psycopg2.Error) as err:
        print(f"{err}try again")


def delete(id):
    try:
        dbCursor = connection.cursor()
        identifier = input("Enter Your Project ID : ")
        updateQuery = f"DELETE FROM details WHERE id = {identifier} AND userid = {id}"
        dbCursor.execute(updateQuery)
        connection.commit()
        dbCursor.close()
    except (Exception,psycopg2.Error) as err:
        print(f"{err}try again")



def DeleteAllProject(id):
    try:
        
        dbCursor = connection.cursor()
        updateQuery = f"DELETE FROM details WHERE userid ={id}"
        dbCursor.execute(updateQuery)
        connection.commit()
        dbCursor.close()
    except (Exception,psycopg2.Error) as err:
        print(f"{err}try again")


def options(id):
    while True:
        print("Menu:")
        print("1. Create Project ")
        print("2. Edit Your Proect ")
        print("3. Add content to exist project ")
        print("4. Delete Your project ")
        print("5. Delete All Project ")
        print("6. Show All Projects ")
        print("7. Log Out")

        choice = input("Enter your choice: ")

        if choice == "1":
            Menu(id)
        elif choice == "2":
            editContent(id)
        elif choice == "3":
            addContent(id)
        elif choice == "4":
            delete(id)
            print("Your project Deleted Successfully.")
        elif choice == "5":
            DeleteAllProject(id)
        elif choice == "6":
            showProject(id)
        elif choice == "7":
            os.system("cls")
            break
        else:
            print("Invalid choice. Please try again.")


mainOptions()