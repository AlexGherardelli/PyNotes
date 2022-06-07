
# %% RECAP
# --- Ricorsione e sue proprietÃ
# --- Esempi: fattoriale, fibonacci, GCD di Eulero, ricerca in una directory

# %% Ricorsione

# decoratore che stampa le chiamate ed uscite di una funzione ricorsiva
import turtle
from rtrace import trace

import random
lista = random.choices(range(-10000, 10001), k=20)

t = turtle.Turtle()

# %%% esempio: mergesort  (ordinamento per fusione)

# osservazione: se ho due liste ordinate Ã¨ facile e veloce unirle in una nuova lista ordinata

# per fondere due liste ordinate
# il primo elemento della soluzione Ã¨ uno dei due primi delle due liste
# il resto della soluzione Ã¨ la fusione del resto delle due liste

# versione ricorsiva


def merge(A, B):
    if not A:           # se A Ã¨ vuota
        return B        # il resto degli elementi Ã¨ in B
    elif not B:         # se B Ã¨ vuota
        return A        # il resto Ã¨ in A
    if A[0] < B[0]:     # altrimenti A e B hanno almeno un elemento, ne confronto i primi
        # e torno il piÃ¹ piccolo seguito dalla fusione del resto
        return [A[0]] + merge(A[1:], B)
    else:
        return [B[0]] + merge(A, B[1:])


def merge_iter(A, B):    # versione iterativa che usa due indici per indicare a quale elemento siamo arrivati
    risultato = []
    indiceA, indiceB = 0, 0     # si parte dalle posizioni 0
    LA = len(A)         # e si termina quando una lista Ã¨ vuota
    LB = len(B)
    # ripeto se entrambe le liste contengono ancora elementi da esaminare
    while indiceA < LA and indiceB < LB:
        if A[indiceA] < B[indiceB]:         # se A contiene l'elemento piÃ¹ piccolo
            risultato.append(A[indiceA])    # lo aggiungo al risultato
            indiceA += 1                    # e passo al suo prossimo elemento
        else:
            risultato.append(B[indiceB])
            indiceB += 1
    # alla fine c'Ã¨ almeno una lista che Ã¨ finita
    risultato += A[indiceA:] + B[indiceB:]  # aggiungo il resto degli elementi
    return risultato

# convergenza: almeno un elemento va a posto per ogni chiamata ricorsiva
# caso base: una delle due liste Ã¨ vuota


A = [1, 34, 67, 345, 1290, 2000]
B = [-23, -2, 17, 40, 400, 4000, 8000]

print(merge(A, B))
print(merge_iter(A, B))


# se ho una lista disordinata e la voglio ordinare:
# la posso spezzare in due liste disordinate (riduzione)
# le posso ordinare separatamente (chiamata ricorsiva sui sottoproblemi)
# le posso fondere rapidamente (costruzione della soluzione)

# @trace
def mergesort(A):
    N = len(A)
    if N < 2:   # se la lista ha 0 o 1 elemento Ã¨ giÃ  ordinata
        return A
    else:
        # A contiene almeno 2 elementi
        metÃ = N//2
        Aordinata = mergesort(A[:metÃ])         # ordino la prima metÃ
        Bordinata = mergesort(A[metÃ:])         # ordino la seconda metÃ
        return merge(Aordinata, Bordinata)      # fondo le due metÃ  ordinate

# convergenza: a forza di spezzare le liste in 2 si arriverÃ  a liste di 0,1 elementi
# caso base:  liste di 1 o 0 elementi, *sono giÃ  ordinate*


print(mergesort(lista))

lista2 = [-34, -45, 56, 23, 90, 43, 1, 200, -234]
mergesort.trace(lista2)


# %%% esempio: alberi binari

# un albero binario Ã¨ fatto da nodi che contengono:
# valore
# figlio sinistro
# figlio destro

class NodoBinario:
    def __init__(self, valore, sx=None, dx=None):
        self._valore = valore
        self._sx = sx
        self._dx = dx

    def __str__(self, livello=0):
        "torno una stringa che rappresenta l'albero indentando i sottoalberi"
        tab = "   "*livello     # livello di indentazione corrente
        risultato = f"{tab}NodoBinario( {self._valore} )"
        if self._sx:
            risultato += f"\n{self._sx.__str__(livello+1)}"
        else:
            risultato += f"\n{tab}   None"
        if self._dx:
            risultato += f"\n{self._dx.__str__(livello+1)}"
        else:
            risultato += f"\n{tab}   None"
        return risultato


# un nodo che non ha figli Ã¨ una foglia
# il nodo che non ha padri Ã¨ la radice
'''
           7
         /   \
        5     6
       / \   / \
      1  2   3  4
'''
n1 = NodoBinario(1)
n2 = NodoBinario(2, n1)
n3 = NodoBinario(3)
n4 = NodoBinario(4)
n5 = NodoBinario(5, n2)
n6 = NodoBinario(6, n3, n4)
n7 = NodoBinario(7, n5, n6)

print(n7)

# %%% stampare un albero binario in preordine/inordine/postordine


def preordine(radice):
    if radice:
        print(radice._valore, end=' ')      # la radice si stampa per prima
        preordine(radice._sx)
        preordine(radice._dx)


preordine(n7)


def inordine(radice):
    if radice:
        inordine(radice._sx)
        # la radice si stampa tra i due sottoalberi
        print(radice._valore, end=' ')
        inordine(radice._dx)


print()
inordine(n7)


def postordine(radice):
    if radice:
        postordine(radice._sx)
        postordine(radice._dx)
        # la radice si stampa dopo entrambi i sottoalberi
        print(radice._valore, end=' ')


print()
postordine(n7)


# %%% visualizzare un albero binario con la turtle

# write del valore sul canvas

def disegna_albero(radice, tartaruga):
    "disegno un albero con la tartaruga"
    if radice:
        # visualizzo il valore leggermente spostato (con degli spazi)
        tartaruga.write(f"    {radice._valore}", font=('Arial', 20, 'bold'))
        if radice._sx:              # se c'Ã¨ un sottoalbero sinistro
            tartaruga.left(30)      # mi giro a SX
            tartaruga.forward(100)  # avanzo di 100 tracciando una linea
            disegna_albero(radice._sx, tartaruga)   # disegno il sottoalbero SX
            tartaruga.backward(100)  # torno indietro
            tartaruga.right(30)     # e mi rimetto nella direzione iniziale
        if radice._dx:              # lo stesso per il sottoalbero DX
            tartaruga.right(30)
            tartaruga.forward(100)
            disegna_albero(radice._dx, tartaruga)
            tartaruga.backward(100)
            tartaruga.left(30)


t.reset()
t.left(90)
disegna_albero(n7, t)

# %%% trovarne l'altezza (il piÃ¹ lungo percorso radice->foglia come numero di nodi)

# se sappiamo l'altezza dei sottoalberi
# ne prendiamo il massimo e sommiamo 1


@trace
def altezza(radice):
    "altezza di un albero, ovvero distanza dalla foglia piÃ¹ lontana alla radice"
    if radice:
        # l'altezza Ã¨ 1+ la massima altezza tra i due sottoalberi
        return max(altezza(radice._sx), altezza(radice._dx)) + 1
    else:
        # l'altezza di un albero vuoto (None) Ã¨ 0
        return 0


print(altezza(n7))

altezza.trace(n7)


# %%% costruire un albero binario completo di N livelli con valori casuali

def crea_binario_completo(N):
    "costruzione di un albero completo di N livelli"
    if N:  # se ancora non sono arrivato in fondo
        valore = random.randint(0, 1000)        # estraggo un valore a caso
        # genero un sottoalbero sinistro completo con un livello di meno
        sinistro = crea_binario_completo(N-1)
        destro = crea_binario_completo(N-1)   # genero il destro
        return NodoBinario(valore, sinistro, destro)    # costruisco la radice
    # altrimenti N==0 e torno None (albero vuoto)


t.reset()
t.left(90)

disegna_albero(crea_binario_completo(5), t)


# %%% costruire un albero binario completo di N livelli con valori che crescono da sinistra a destra

def crea_binario_completo_ordinato(N, numero):
    if N:
        sinistro, quanti = crea_binario_completo_ordinato(N-1, numero)
        destro, quantiDX = crea_binario_completo_ordinato(N-1, quanti+1)
        return NodoBinario(quanti+1, sinistro, destro), quantiDX
    else:
        return None, numero


t.reset()
t.left(90)

albero, nodi = crea_binario_completo_ordinato(4, 0)

disegna_albero(albero, t)

inordine(albero)

# %%% creare un albero binario casuale con max N livelli

# SE N: con probabilitÃ  X% creo il sottoalbero sx o dx di N-1 livelli


def crea_albero_random(N, prob):
    # se non sono ancora arrivato al livello 0 (alberi vuoti)
    # ed estraggo a sorte un valore minore della prob
    if N and random.randint(1, 100) <= prob:
        valore = random.randint(-100000, 100000)    # creo un valore a caso
        # genero a caso il sottoalbero SX con al piÃ¹ N-1 livelli
        sx = crea_albero_random(N-1, prob)
        dx = crea_albero_random(N-1, prob)          # e anche il DX
        return NodoBinario(valore, sx, dx)          # e costruisco la radice
    # altrimenti torno None


t.reset()
t.left(90)
AL = crea_albero_random(4, 70)
disegna_albero(AL, t)

# %%

print(altezza(AL))

# %%% calcolare il DIAMETRO di un albero (piÃ¹ lungo percorso da foglia a foglia)

# il percorso piÃ¹ lungo poterebbe:
# passare per la radice:
# la sua lunghezza Ã¨ 1 + la somma delle due altezze maggiori a sx e dx
# non passare per la radice
# allora Ã¨ tutto nel sottoalbero sx
# oppure tutto nel sottoalbero dx
# vanno confrontati tutti e 3 per trovare il massimo
# caso base: una foglia ha percorso 0


def diametro(radice):
    # se il nodo esiste
    if radice:
        # vedo quanto Ã¨ lungo il percorso massimo completamente contenuto nel sottoalbero SX
        SX = diametro(radice._sx)
        # e nel destro
        DX = diametro(radice._dx)
        # e calcolo il massimo percorso se invece si passa per la radice
        Asx = altezza(radice._sx)   # altezza massima a SX
        Adx = altezza(radice._dx)   # altezza massima a DX
        # il percorso massimo che passa per la radice Ã¨ la loro somma +1
        RAD = Asx + Adx + 1
        return max(SX, DX, RAD)     # torno il massimo tra questi 3 valori
    else:
        # altrimenti questo Ã¨ un albero vuoto
        return 0                    # che ha percorso massimo lungo 0 nodi


print(diametro(AL))

# nota: possiamo PRIMA trovare la altezza massima a partire da ciascun nodo
#       in modo da averle a disposizione mentre cerchiamo i percorsi massimi


# %%% GIOVEDI':  alberi n-inari e directory

# un albero N-ario Ã¨ fatto da nodi che contengono:
# valore
# 0 o piÃ¹ figli

# %%% esempio: albero n-ario costruito a partire da una directory

# %%% visualizzare un albero n-ario con la turtle
