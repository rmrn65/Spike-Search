# Spike-Search
Spike-Search este o aplicatie folosita pentru a gasi cuvinte in 
fisierele dintr-un director prestabilit de utilizator

## Necesitati
Pentru ca totul sa functioneze in parametrii normali trebuie ca
in cazul in care nu ai instalat pip3 sa inserezi urmatoarea comanda
...
sudo apt install python3-pip
...
Pentru a verifica daca s-a instalat introdu comanda
...
pip3 --version
pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)
...

## Instalare si rulare
Pentru a instala aplicatia trebuie rulata comanda 
...
make config
make build
...
In urma rularii comenzi se va crea un executabil Spike-Search
Pentru rulare se va introduce comanda  
...
make run 
...
sau
...
./Spike-Search
...
## Utilizare 
Dupa rularea aplicatiei prima fereastra va cere un numele folderului 
in care se afla fiseirele in care vrei sa cauti.

**Atentie folderul nu trebuie sa contina la final caracterul "/", 
aplicatia stie deja ca este vorba despre un folder sau o cale catre 
unul**

In bara urmatoare veti putea cauta cuvintele, iar prin apasarea lui
Enter sau butonului de Search veti primi linkuri catre fisierele care
contin stringul coresupnzator cautarii. La apasarea acestor linkuri, 
documentul va fi deschis

_Ii doresc bafta lui Dorin si sper sa puna vorba aia buna mentorilor :)_



## Despre aplicatie ( detalii )
Aplicatia este scrisa in Python si foloseste numpy pentru a manipula
vectorii si calculul cu acestia. 
La introducerea query-urilor este creata o matrice care are cuvintele 
cautate, pe coloane si documentele in care se cauta, pe linii. Se 
introduce 0 daca cuvantul nu exista in fisier si 1 daca exista.
Interfata grafica foloseste PyQt5. Ferestrele sunt create cu ajutorul
claselor.
