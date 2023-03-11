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


# userinfo = input ('your full name Or email  >>>>  ').strip()
# userpass = input (' your passwd             >>>>  ').strip()

# # mohammed@gmail.com
# # 1111111111
# user = ()
# try:
#     dbCursor = connection.cursor()
#     sql = "select * from users where email = %s  and passwd = %s ;"
#     data = (userinfo,userpass)
#     dbCursor.execute(sql,data)
#     user = dbCursor.fetchone()
    
# except (Exception,psycopg2.Error) as err:
#     print(f"{err}try again")
# print(user)
# projects = []
# user = (1,'mohammed','Badr','1111111111','11111111111','mohammed@gmail.com')
# print(str(user[0]))
# print(user[0])
# print(type(user[0]))
# try:
#     dbCursor = connection.cursor()
#     sql = "select  *  from projects where user_id =  %s ;"
#     dbCursor.execute(sql,str(user[0]))
#     projects = dbCursor.fetchall()
# except (Exception,psycopg2.Error) as err:
#     print(f"{err}  try again")
# for x in range(0,len(projects)) :
#     print(f'{x + 1} ) {projects[x][0]}' )
# def selectbyname(name , id):
#     print(name)
#     print(id)
#     project = ''
#     try:
#         dbCursor = connection.cursor()
#         sql = "select * from projects  WHERE name = %s AND user_id = %s ;"
#         # sql = f"SELECT * FROM projects WHERE user_id = {id} and name = {name}"
#         data = (name , id)
#         dbCursor.execute(sql , data)
#         project = dbCursor.fetchone()
        
#     except (Exception,psycopg2.Error) as err:
#         print(f"{err}try again")
#     return project
# name = 'updat'


# showfilecontent = selectbyname(name ,1)

# for x in showfilecontent   :
#     print(f' | {x}  |') 
id = 1
name = 'shop'
try:
    dbCursor = connection.cursor()
    sql = "delete from projects where user_id = %s and name = %s ;"
    dbCursor.execute(sql,(id , name))
    project = dbCursor.fetchall()
    print(project)
except (Exception,psycopg2.Error) as err:
    print(f"{err} try again")