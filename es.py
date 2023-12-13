prenotazioni=()

def aggiungi_prenotazioni(prenotazioni):
    nome=input("Inserisci un nome:  ")
    data=input("Inserisci una data: ")
    numP=int(input("Inserisci il numero di persone: "))
    numT=int(input("Inserisci il numero del tavolo: "))
    prenotazioni.add(nome,data,numP,numT)
    return (prenotazioni)

def rimuobi_prenotazioni(prenotazioni):
    nome=input("Inserisci un nome:  ")
    data=input("Inserisci una data: ")
    
#nom,dat,numeroP,numeroT=aggiungi_prenotazioni(prenotazioni)
print(aggiungi_prenotazioni(prenotazioni))
#def rimuovi_prenotazioni()