import json
import re
import time
import os
import sqlite3
import psycopg2
dbUser = 'postgres'
dbName = 'dblab'
dbPassword = '123'

connection = psycopg2.connect(
    host="127.0.0.1",
    database=dbName,
    user=dbUser,
    password=dbPassword,
    )


def selectbyname(name , id):
    project = ''
    try:
        dbCursor = connection.cursor()
        sql = "select * from projects  WHERE name = %s AND user_id = %s ;"
        
        data = (name , id)
        dbCursor.execute(sql , data)
        project = dbCursor.fetchone()
        
    except (Exception,psycopg2.Error) as err:
        print(f"{err}try again")
    return project


def showAllproject(id):
    print(id)
    projects = []
    try:
        dbCursor = connection.cursor()
        sql = "select  *  from projects where user_id =  %s ;"
        dbCursor.execute(sql,str(id))
        projects = dbCursor.fetchall()
    except (Exception,psycopg2.Error) as err:
        print(f"{err}  try again")
    for x in range(0,len(projects)) :
        print(f'{x + 1} ) {projects[x][0]}' )
 


def returnAllproject(id , name):
    print(id,name)
    project = []
    try:
        dbCursor = connection.cursor()
        sql = "select * from projects where user_id = %s and name = %s ;"
        dbCursor.execute(sql,(id , name))
        project = dbCursor.fetchall()
        
    except (Exception,psycopg2.Error) as err:
        print(f"{err} try again")
    print(project)
    for p in project :
        if name == p[0] :
            return True
            break
   
   
def dealwithprojects(id):
    id = id
    while True :
        print('show all project')
        choice = input('what do you want choose one of the following \n\npress 1 to show project \npress 2 to update project \npress 3 to delete project  \n or q to back \n >>>> ')
        match choice:
                case 'q' :
                    break
                case "1":
                    
                    while True:
                        
                        print("show project ")
                        showAllproject(id)
                        
                        project = input('write project name that you want to show it Or q to back  >>>>  ')
                        
                        
                        if project == 'q':
                            os.system('cls')
                            break
                        elif returnAllproject(id , project):
                            
                            print('project is exist')
                            print('')
                            showfilecontent = selectbyname(project,id)
                            
                            for x in showfilecontent   :
                                print(f' | {x}  |') 
                                
                            break
                        else :
                            
                            print('file is not exist')
                case "2":
                   
                    while True:
                        os.system('cls')
                        print("update project ")
                        showAllproject(id)
                        project = input('write project name that you want to update it Or q to back  >>>>  ')
                        if project == 'q':
                            os.system('cls')
                            break
                        elif returnAllproject(id , project):
                            os.system('cls')
                            print('project is exist')
                            showfilecontent = selectbyname(project , id)
                            print('')
                            
                            newname = input('new name is :- ')
                            newdescription = input('new description is :- ')
                            newtotal = ''
                            while True:
                                newtotal = input('new total is :- ')
                                if newtotal.isdigit() :
                                    break
                                else:
                                    print(' total must be digit ')  
                            try:
                                dbCursor = connection.cursor()
                                sql = "UPDATE projects SET name= %s, des= %s, total= %s WHERE user_id = %s and name = %s ;"
                                dbCursor.execute(sql,(newname , newdescription ,newtotal , id , project ))
                                connection.commit()
                            
                            except (Exception,psycopg2.Error) as err:
                                print(f"{err}try again")
                            
                        else :
                            os.system('cls')
                            print('file is not exist')
                            
                case '3':
                    
                    while True:
                        
                        print("delete project ")
                        showAllproject(id)
                        project = input('write project name that you want to update it Or q to back  >>>>  ').strip()
                        print(returnAllproject(id , project))
                        if project == 'q':
                            os.system('cls')
                            break
                        elif returnAllproject(id , project):
                            try:
                                dbCursor = connection.cursor()
                                sql = "delete from projects where user_id = %s and name = %s ;"
                                dbCursor.execute(sql,(id , project))
                                connection.commit()
                                
                            except (Exception,psycopg2.Error) as err:
                                print(f"{err}try again")
                            print('project has been deleted')
                        else:
                            
                            print('file is not exist')



def signin():
    os.system('cls')
    print('signin')
    trials = 4
    # check if the user have file  
    while trials != 0 :
        userinfo = input ('your full name Or email  >>>>  ').strip()
        userpass = input (' your passwd             >>>>  ').strip()
  
        trials -=1
       
        user = ()
        try:
            dbCursor = connection.cursor()
            sql = "select * from users where email = %s  and passwd = %s ;"
            data = (userinfo,userpass)
            dbCursor.execute(sql,data)
            user = dbCursor.fetchone()
            
        except (Exception,psycopg2.Error) as err:
            print(f"{err}try again")
        print(user)
        if trials != 0 :
            if user  :
                print(f'welcome {user[1]} ')
                while True:
                            print('what do you want >>>  ')
                            choice = input('press 1 to deal with  projects \npress 2 to create project  ')
                            if choice == '1':
                                projects = []
                              
                                try:
                                    dbCursor = connection.cursor()
                                    sql = "select  *  from projects where user_id =  %s ;"
                                    dbCursor.execute(sql,str(user[0]))
                                    projects = dbCursor.fetchall()
                                except (Exception,psycopg2.Error) as err:
                                    print(f"{err}  try again")

                                if    len(projects) == 0 :
                                    print('there is no projects')
                                else:
                                    for x in range(0,len(projects)) :
                                        print(f'{x + 1} ) {projects[x][0]}' )
                                    dealwithprojects(user[0])
                                    pass
                            elif choice == '2':
                            
                                projectName = input('projectname >>>  ')
                                description = input('enter the description of project  >>   ')
                                while True:
                                    if len(description) < 10 :
                                        print('the descripton can not be than 10 characters !')
                                        description = input('enter the description of project  >>   ')
                                    else :
                                        break
                                total = input('enter the total of project  >>   ')
                                while True:
                                    if total.isdigit() :
                                        break
                                    else :
                                        print('the Total must be numbers !')
                                        total = input('enter the total of project  >>   ')
                                try:
                                    dbCursor = connection.cursor()
                                    sql = "INSERT INTO projects(name, des, total, user_id)VALUES (%s, %s, %s, %s);"
                                    data = (projectName,description,total,user[0])
                                    user = dbCursor.execute(sql,data)
                                    connection.commit()
                                    
                                except (Exception,psycopg2.Error) as err:
                                    print(f"{err}try again")
                            else:
                                print('out of options')
              
            else :
                os.system('cls')
                print(f'your are not exist \ you still have {trials} trials ')
        else :
            os.system('cls')
            print('try again later')
            break
    else :
        print('try again later ')




# sign up project

def signup():
    fname , lname , email , passwd , repasswd , phone = '','','','','',''
    while True :
            fname = input ('write first name ?')
            if len(fname) == 0 :
                print('first name con not be empty ')
            else :
                break
    while True :
            lname = input ('write last name ?')
            if len(lname) == 0 :
                print('last name con not be empty ')
            else :
                break
    while True :
            email = input ('write first email ?')
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            if not email.isdigit() :
                if  len(email)  == 0 :
                    print('email can not be empty')
                    
                elif not re.fullmatch( regex ,email ):
                    print('please enter valide email ')
                else :
                    break   
            else :
                print('invalide input') 
    while True :
            passwd = input ('write  passwd >> ')
            if len(passwd) == 0 :
                print('passwd can not be empty >> ')
            elif len(passwd) < 8 :
                print('passwd can not be empty >> ')
            else :
                print('ok')
                break
    while True :
            repasswd = input ('rewrite passwd >> ')
            if repasswd != passwd :
                print('passwd and repasswd not match ')
            else :
                break
    while True :
            phone = input ('write your phone >>  +20 ')
            if not phone.isdigit() :
                print('phone must be number not string ')
            elif len(phone) < 10 :
                print('invalide phone')
            elif len(phone) > 10 :
                print('invalide phone')
            else:
                break
    
    try:
        dbCursor = connection.cursor()
        sql = "INSERT INTO users( fname, lname, passwd, phone, email) VALUES (%s, %s, %s, %s, %s);"
        data = (fname,lname,passwd,f'+20{phone}',email)
        dbCursor.execute(sql,data)
        connection.commit()
    except (Exception,psycopg2.Error) as err:
        print(f"{err}try again")
    

