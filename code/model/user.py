from .meal import conn
c=conn.cursor()


users4data_name=[]
users4data_surname=[]
users4data_phonenumber=[]
def listAllUsers():
    c.execute('SELECT name FROM users_object')
    for i in c.fetchall():
        users4data_name.append(i)
  
    c.execute('SELECT surname FROM users_object')
    for j in c.fetchall():
  
        users4data_surname.append(j)
    c.execute('SELECT phone_number FROM users_object')
    for k in c.fetchall():
        users4data_phonenumber.append(k)
    
    conn.commit()


new_added_user_name=[]
new_added_user_surname=[]
new_added_user_phone=[]
user_ime=[]
user_prezime=[]
user_broj=[]
def addUser(name,surname,phone_number):
    new_added_user_name.clear()
    new_added_user_surname.clear()
    new_added_user_phone.clear()
    new_added_user_name.append(name)
    new_added_user_surname.append(surname)
    new_added_user_phone.append(phone_number)
    c.execute("INSERT into users_object (name, surname,phone_number) values (?,?,?)",(name,surname,phone_number))
    print("new added......",new_added_user_name)
    #c.execute('SELECT name FROM meal_object')

    conn.commit()
f=conn.cursor()
def NumberOFUsers():
    br=0
    c.execute('SELECT name FROM users_object')
    for i in c.fetchall():
         br=br+1
    return br



