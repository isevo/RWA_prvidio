# from . import db
import sqlite3
conn=sqlite3.connect('meal.db',check_same_thread=False)


c=conn.cursor()
meals4data_name=[]
meals4data_price=[]
def listAll():
    c.execute('SELECT name FROM Meal')
    for i in c.fetchall():
        print(i[0])
        meals4data_name.append(i[0])
        print(i)
    c.execute('SELECT price FROM Meal')
    suma=0
    for j in c.fetchall():
        print(j[0])
        meals4data_price.append(j[0])
       # suma=j[0]+suma
   # print("suma ",suma)
    conn.commit()
    

new_added_meal_name=[]
new_added_meal_price=[]
jelo_ime=[]
jelo_cijena=[]
def addArgument(name,price):
    new_added_meal_name.clear()
    new_added_meal_price.clear()
    new_added_meal_name.append(name)
    new_added_meal_price.append(price)
    ########################################
    name=str(name)
    price=str(price)
    c.execute("INSERT into Meal (name, price) values (?,?)",(name,price))
    print("new added......",new_added_meal_name)
    #c.execute('SELECT name FROM meal_object')

    conn.commit()


