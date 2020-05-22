# PROJEKT PRVI DIO


### O PROJEKTU
Projekt se sastoji od tri glavne mape(controller,model,service).
U mapi controller se nalaze controleri za jelo,korisnika i rezervaciju stola u kojima
se nalaze get i set metoda te update za rezervaciju stola.


U mapi service sam napravila provjeru unesenog tokena.

U mapi model se nalaze sql upiti za bazu (dodavanje, citanje i update podataka).

Prvo treba otici na http://127.0.0.1:5000/login . Password je password7, nakon uspjesnog logiranja, dobije se token
 koji omogucava pristup metodama u api-u. Od metoda koje sam koristila su get za dodavanje korisnika i jela u bazu te njihov ispis iz baze
 preko get metoda. Za dodavanje korisnika treba napisati njegovo ime,prezime i broj mobitela. A za dodavanje jela.naziv i cijenu.
 Za rezervaciju stola sam napravila update i get.U bazi postoji 10 stolova od kojih su neki rezervirani i pise id 
 korisnika koji ih je rezervirao,a neki nisu rezervirani i uz takve je id korisnika naveden kao 0.
 Za rezervaciju stola je potrebno napisati id osobe ,broj stola i YES ako se stol zeli rezervirati tj NO ako se zeli maknuti rezervacija.
 Get metoda izbacuje sve stolove bilo da su rezervirani ili ne.


#### Pokretanje
<ol>
<li>instalacija venv-a</li>
<li>instalacija requirementsa</li>
<li>set FLASK_APP=myapp.py</li>
<li>flask run</li>
<li> http://127.0.0.1:5000/login i logirati se (password7),pa pokupiti token</li>
<li>Otici na http://127.0.0.1:5000/ i pokrenuti api </li>
</ol>

