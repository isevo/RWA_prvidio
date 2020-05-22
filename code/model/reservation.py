from .meal import conn
from .user import NumberOFUsers
c=conn.cursor()

d=conn.cursor()


tabels_number=[]
id_person_reservations=[]
y_n_reservation=[]

def listAllDeskReservation():
    c.execute("SELECT number,id_person,rezervated FROM tabels")
    for el in c.fetchall():
        tabels_number.append(el[0])
        id_person_reservations.append(el[1])
        y_n_reservation.append(el[2])
    print(y_n_reservation)


addNumberofTable=[]
addIdPerson=[]
broj_stola=[]
id_osobe=[]
rezervacija=[]
#broj stola i id osobe
def ReservateTable(number,id_person,rezervacija):
    
    rezervated='YES'
    if rezervacija=="NO":
        c.execute("UPDATE tabels SET  id_person = ?, rezervated = ? where number = ? AND rezervated = ?",(0,'NO',number,'YES'))
        numb=NumberOFUsers()
        addNumberofTable.clear()
        addIdPerson.clear()
        addNumberofTable.append(number)
        addIdPerson.append(id_person)
        conn.commit()
        return "stol rezerviramo"
    elif  rezervacija=="YES":
        c.execute("UPDATE tabels SET  id_person = ?, rezervated = ? where number = ? AND rezervated = ?",(id_person,'YES',number,'NO'))
        numb=NumberOFUsers()
        addNumberofTable.clear()
        addIdPerson.clear()
        addNumberofTable.append(number)
        addIdPerson.append(id_person)
        conn.commit()
        return "stol rezerviramo"
    else:
        return 'cdcdh'

  
    conn.commit()
        

