#MEDIA VOTI DI N STUDENTI
"""1.Creare un dizionario di N studenti.
Ogni elemento del dizionario contiene come chiave il nome
dello studente e come valore una lista di tre numeri, cioè
i voti in [Matematica, Fisica e Chimica].
2.Inserendo il nome di uno studente, il programma restituisce
in output la media dei suoi voti
(arrotandata a due cifre dopo la virgola)."""

studenti={}
media=0


def aggiungi_voti(studenti):
    Mate=""
    Fisica=""
    Chimica=""
    media=0
    for i in range (nStud):
        nomeStud=input("Inserisci il nome dello studente:")
        studenti[nomeStud]=nomeStud
        Mate=int(input("Inserisci il voto per matematica:"))
        Fisica=int(input("Inserisci il voto per fisica:"))
        Chimica=int(input("Inserisci il voto per chimica:"))
        studenti[nomeStud]=[Mate,Fisica,Chimica]
        media+=studenti[nomeStud][i]
    media=media/3
    return studenti,media


nStud=int(input("Inserisci il numero di studenti:"))
votiStud,mediaS=aggiungi_voti(studenti)
print(votiStud)
nomeMedia=input("Inserisci il nome di uno studente per calcolarne la media:")
for nome in studenti.keys():
    print(nome)
    if(nomeMedia==studenti[nome]):
        print("La media dello studente:",nomeMedia,"è di:",mediaS)
    else:
        print("Studente inesistente")