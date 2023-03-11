import psycopg2
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


dealwithprojects(1)

