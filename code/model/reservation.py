from .meal import conn
from .user import NumberOFUsers
c=conn.cursor()

d=conn.cursor()


tabels_number=[]
id_person_rezervations=[]
y_n_rezervation=[]

def listAllDeskRezervation():
    c.execute("SELECT number,id_person,rezervated FROM tabels")
    for el in c.fetchall():
        tabels_number.append(el[0])
        id_person_rezervations.append(el[1])
        y_n_rezervation.append(el[2])
    print(y_n_rezervation)


addNumberofTable=[]
addIdPerson=[]
broj_stola=[]
id_osobe=[]
rezervacija=[]
#broj stola i id osobe
def RezervateTable(number,id_person,rezervacija):
    
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
        

