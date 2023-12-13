voti={}

media=0

def aggiungi_voti(voti,numVoti,media):
    cont=0
    for i in range (numVoti):
        materia=input("Inserisci una materia:")
        voto=int(input("Inserisci il voto:"))
        voti[materia]=voto
        cont+=1
        print(cont)
        media+=voti[materia]
        print(media)
    media=media/cont
    return voti,media


        
numVoti=int(input("Inserisci il numero di voti da inserire:"))
risVoti,mediaVoti=aggiungi_voti(voti,numVoti,media)
print(voti)
for voto in voti.keys(): 
    print(f"-{voto}:{risVoti[voto]}")
print(f"media voti:{mediaVoti}")