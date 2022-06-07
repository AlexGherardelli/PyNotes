# %% RECAP
# --- try/except/finally e definizione di nuovi tipi di errori
# --- espressioni algebriche semplici ed alberi binari
# ---- costruzione dell'albero da una espressione algebrica (parser)
# ---- visualizzazione dell'abero con la turtle

# DA FARE IN UNA LEZIONE SUCCESSIVA: semplificazione algebrica e derivate

# %%% init

# decoratore che stampa le chiamate ed uscite di una funzione ricorsiva
# from rtrace import trace

import random 
lista = random.choices(range(-10000,10001), k=10)

# %% alberi n-ari : con 0 o piÃ¹ figli
    
class AlberoNArio:
    def __init__(self, valore, figli=None):     # MAI inizializzare un valore di default con un valore mutabile
        "Ogni nodo contiene un valore e puÃ² avere dei figli"
        if figli is None:                       # MEGLIO: se il valore non Ã¨ stato passato
            figli = []                          # lo inizializzo qui con una nuova lista vuota
        self._valore = valore
        self._figli  = figli

    def __repr__(self, livello=0):
        "stringa usata per stampare il nodo (con indentazione)"
        risultato = '|--'*livello + f"AlberoNArio({self._valore})"
        for son in self._figli:     # per ogni figlio
            risultato += '\n' + son.__repr__(livello+1)     # aggiungo una riga con il figlio piÃ¹ indentato
        return risultato

# %%% Esempio

n1 = AlberoNArio(1)
n2 = AlberoNArio(2)
n3 = AlberoNArio(3)
n4 = AlberoNArio(4)
n5 = AlberoNArio(5, [n1, n2, n3, n4])

print(n5)

# %%% esempio: albero n-ario costruito a partire da una directory

# un albero N-ario Ã¨ fatto da nodi che contengono:
    # valore
    # 0 o piÃ¹ figli

class AlberoFS:
    def __init__(self, valore, isFile, figli=None):
        if figli is None:
            figli = []
        self._valore = valore
        self._figli  = figli
        self._isFile = isFile           # ogni path puÃ² essere un file (True) oppure una directory (False)

    def __repr__(self, livello=0):
        risultato = '|--'*livello + f"AlberoFS({self._valore}, {self._isFile},...)"
        for son in self._figli:
            risultato += '\n' + son.__repr__(livello+1)
        return risultato

import os
def genera_albero(path):
    if not os.path.isfile(path):    
        figli = []
        for nome in os.listdir(path):
            fullname = path + '/' + nome
            if os.path.isfile(fullname):
                figli.append(AlberoFS(fullname, True))
            else:
                figli.append(genera_albero(fullname))
        return AlberoFS(path, False, figli)
    else:
        return AlberoFS(path, True, [])
    

D = genera_albero('..')
print(D)

print(genera_albero('lezione20.py'))

# %%% visualizzare un albero n-ario con la turtle (NO)

# stavolta disegnamo per livelli
# in modo che ci sia abbastanza spazio per ciascun sottoalbero
    # prima dobbiamo calcolare lo spazio necessario per i sottoalberi
    # poi potremo posizionarli e collegarli alla radice

# %%% altezza di un albero N-ario (facile)

# caso base: la radice ha altezza 1
# l'altezza massima Ã¨ data dal massimo delle altezze dei figli + 1 

def altezza(radice):
    if not radice._figli:
        return 1
    else:
        return max( [altezza(figlio) for figlio in radice._figli ] ) + 1

print(altezza(D))

# %%% diametro di un albero N-ario (medio)
# il percorso piÃ¹ lungo puÃ² essere completamente in uno dei sottoalberi (chiamata ricorsiva)
# oppure passare per la radice (in questo caso servono le 2 massime altezze + 1)

def diametro(radice):
    if not radice._figli:
        return 1
    else:
        # prima trovo il valore del diametro massimo di ciascuno dei sottoalberi
        diam_max_figli = max([ diametro(figlio) for figlio in radice._figli ])
        # poi calcolo la lunghezza del percorso se passasse per la radice
        if len(radice._figli) == 1:             # se c'Ã¨ un solo figlio
            # altezza dell'unico sottoalbero +1
            diametro_per_radice = 1 + altezza(radice._figli[0])
        else:
            # se ci sono almeno 2 figli prendo le prime due altezze massime
            altezze_ordinate = list(sorted([ altezza(figlio) for figlio in radice._figli ], reverse=True ))
            prima, seconda = altezze_ordinate[:2]
            diametro_per_radice = prima + seconda + 1       # e il percorso piÃ¹ lungo Ã¨ la loro somma +1
        return max(diametro_per_radice, diam_max_figli)     # torno il massimo dei due casi (per la radice o solo nei sottoalberi)


n1 = AlberoNArio(1)
n2 = AlberoNArio(2)
n3 = AlberoNArio(3, [n1, n2])
n4 = AlberoNArio(4, [n3])
n5 = AlberoNArio(5, [n4])
n6 = AlberoNArio(6)
n7 = AlberoNArio(7, [n5, n6])

print(n7)
print(diametro(n7))

# %% Alberi di gioco n-ari (per rappresentare le diverse "configurazioni" di una partita con regole di gioco)

# %%% fusione di coppie pari+pari o dispari+dispari

# data una lista di valori interi: 
    # mossa: se due valori consecutivi sono entrambi pari o entrambi dispari li sommo
    # termino quando non posso piÃ¹ sommare 
    # caso base/foglia, non posso piÃ¹ applicare la mossa (sono alternati o uno solo)
    # convergenza: ad ogni passo diminuisco di 1 il numero di elementi della lista -> lista con 1 el

# configurazione: lista di valori + figli
class Sequenza:
    def __init__(self, lista):
        "Una configurazione contiene la lista di interi"
        self._lista = lista
        self._figli  = []

    def __repr__(self, livello=0):
        risultato = '|--'*livello + f"{self._lista}"
        for son in self._figli:
            risultato += '\n' + son.__repr__(livello+1)
        return risultato

    def mosse_valide(self):
        "elenco di tutte le posizioni i,i+1 che possono essere sommate"
        return [ i for i in range(len(self._lista)-1) 
                # mossa valida se resti uguali (pari+pari o dispari+dispari)
                if self._lista[i]%2 == self._lista[i+1]%2 ] 

    def applica_mossa(self, i):
        "applico una mossa creando il figlio ed aggiungendolo ai figli"
        nuova_lista = self._lista.copy()    # copio la sequenza per non modificarla
        # rimpiazzo i due valori con la loro somma usando un assegnamento a slice
        nuova_lista[i:i+2] = [nuova_lista[i] + nuova_lista[i+1]]
        # creo il nuovo nodo e lo aggiungo ai figli
        self._figli.append(Sequenza(nuova_lista))

    def genera(self):
        "applicazione delle mosse valide e generazione dei sottoalberi"
        for i in self.mosse_valide():
            self.applica_mossa(i)
        for figlio in self._figli:
            figlio.genera()
            
    def shortest(self):
        "minima altezza, ovvero distanza della foglia piÃ¹ vicina dalla radice"
        if not self._figli:
            return 1, self
        else:
            return min( figlio.shortest() for figlio in self._figli ) + 1
    
    def tallest(self):
        "massima altezza, ovvero distanza della foglia piÃ¹ lontana dalla radice"
        if not self._figli:
            return 1, self
        else:
            return max( figlio.tallest() for figlio in self._figli ) + 1

    def tallest_2(self):
        "massima altezza E foglia che gli corrisponde"
        if not self._figli:     # se sono una foglia
            return 1, self      # torno 1 e me stessa
        else:
            # altrimenti calcolo le distanze massime per ciascun figlio
            altezze_figli = [ figlio.tallest_2() for figlio in self._figli ]
            # e tra queste prendo la coppia massima con la foglia corrispondente
            massimo, nodo = max(altezze_figli, key=lambda coppia: coppia[0])
            # torno la distanza massima +1 e quella foglia
            return massimo + 1, nodo

    def shortest_2(self):
        "minima altezza e foglia che la produce"
        if not self._figli:
            return 1, self
        else:
            altezze_figli = [ figlio.shortest_2() for figlio in self._figli ]
            minimo, nodo = min(altezze_figli, key=lambda coppia: coppia[0])
            return minimo + 1, nodo

# metodi:
    # __repr__
    # mosse possibili
    # applicazione di una mossa per ottenere una nuova configurazione
    # generazione dell'albero, prima i figli diretti, poi si scende
    # profonditÃ  minima e massima
    # insieme di tutte le foglie diverse

# %%%% Esempio: cercare la sequenza di mosse (altezza) piÃ¹ breve e quella piÃ¹ lunga

L = [ 1, 2, 3, 7, 8, 12, 7, 5, 9, 6]
A = Sequenza(L)
A.genera()

print(A)
print(A.shortest(), A.tallest())

import random

for i in range(20):
    lista = random.choices( range(1000000), k=10 )
    A = Sequenza(lista)
    A.genera()
    if A.shortest() != A.tallest():
        print(lista)
# %%

# questa sequenza ha un albero di gioco con altezza massima diversa dall'altezza minima
B = Sequenza([933420, 831712, 421486, 116868, 424017, 714059, 653101, 38261, 212454, 618012])
B.genera()

print(B.shortest_2(), B.tallest_2())
#print(A.foglie())

#--------------------------------------------------------------------------------

# %%% altro esempio: fusione di coppie pari+dispari

# basta cambiare la generazione delle mosse valide

#--------------------------------------------------------------------------------

# %%% gioco degli anagrammi: date due stringhe A e B una l'anagramma dell'altra
# ---- in ogni posizione di gioco si possono scegliere 2 lettere qualsiasi e scambiarle
# ---- il gioco termina quando la prima parola Ã¨ uguale alla seconda
# ---- trovare l'altezza minima (ovvero una soluzione con meno scambi)

# posizione di gioco: due stringhe
# caso base: se le due stringhe sono uguali ho trovato la soluzione, torno il livello
# altrimenti provo a scambiare due caratteri in modo da metterne almeno uno a posto (convergenza)
   # (cerco il primo carattere in A diverso in B, lo trovo in B e li scambio)
   # creo le configurazioni figlie di ciascun nodo creato
# alla peggio con N scambi trasformo A in B

class Anagramma:
    
    # s1 ed s2 sono liste di caratteri
    def __init__(self, s1, s2):
        "memorizzo le sequenze di caratteri per cui devo trovare la sequenza di scambi"
        assert list(sorted(s1)) == list(sorted(s2)), "Non sono anagrammi" 
        self._s1 = s1
        self._s2 = s2
        self._figli = []

    def __repr__(self, livello=0):
        "torno la stringa da stampare per visualizzare il nodo ed i figli"
        risultato = '|--'*livello + f"{self._s1} {self._s2}"
        for son in self._figli:
            risultato += '\n' + son.__repr__(livello+1)
        return risultato
        
    def mosse_valide(self):
        "Genero l'insieme di mosse valide"
        if self._s1 == self._s2:    # se sono giÃ  uguali 
            return set()            # non c'Ã¨ da fare scambi
        else:
            mosse = set()           # altrimenti
            for i,c1 in enumerate(self._s1):            # scandisco _s1 
                if c1 != self._s2[i]:                   # se nella stessa posizione il carattere di s2 Ã¨ diverso
                    for j in range(len(self._s1)):      # cerco una posizione
                        if j!=i and self._s2[j] == c1:  # con indice diverso che contiene il carattere cercato
                            # se la mossa non Ã¨ stata giÃ  generata ( (i,j) equivale a (j,i) )
                            if (j,i) not in mosse:
                                mosse.add((i,j))        # la aggiungo
            return mosse

    def applica_mossa(self, i, j):
        "Applico una mossa generando un figlio"
        nuova_s1 = self._s1.copy()                          # copio _s1 per non modificarla
        # scambio i valori che stanno nei due indici
        nuova_s1[i], nuova_s1[j] = nuova_s1[j], nuova_s1[i]
        self._figli.append(Anagramma(nuova_s1, self._s2))   # creo la nuova configurazione e la aggiungo ai figli

    def genera(self):
        "Applico tutte le mosse valide e poi lo faccio sui figli generati"
        for i,j in self.mosse_valide():
            self.applica_mossa(i,j)
        for figlio in self._figli:
            figlio.genera()

    def min_mosse(self):
        "altezza minima (come numero di archi)"
        if not self._figli:
            return 0
        else:
            return 1 + min(son.min_mosse() for son in self._figli)

A1 = Anagramma(list("bedca"), list("abcde"))
A1.genera()

print(A1)
print(A1.min_mosse())

#--------------------------------------------------------------------------------

# %%% gioco del resto con le monete
# --- dato un valore intero N (resto da dare) 
# --- ed una lista ordinata L di valori interi di monete che contiene sempre 1 (es [10, 5, 2, 1])
# --- trovare i diversi modi di dare il resto
# ------ Esempio: N = 9, L = [10, 5, 2, 1]
# 9 = 5 + 2 + 2
# 9 = 5 + 2 + 1 + 1
# 9 = 5 + 1 + 1 + 1 + 1
# 9 = 2 + 2 + 2 + 2 + 1
# 9 = 2 + 2 + 2 + 1 + 1 + 1
# 9 = 2 + 2 + 1 + 1 + 1 + 1 + 1
# 9 = 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1
# 9 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

# casi base: N == 1 oppure M == [1] 
# se M[0] > N  ignoro la prima moneta
# altrimenti provo a usarla
# altrimenti provo a non usarla mai
# convergenza: sottraggo sempre qualcosa minore o uguale ad N da N

class Resto:
    def __init__(self, N, LM, mossa=0):
        "una configurazione contiene un valore e la lista di monete disponibili e puÃ² ricordare la moneta usata per arrivare qui"
        self._N = N
        self._LM = LM
        self._figli = []
        self._mossa = mossa

    def __repr__(self, livello=0):
        "torno la stringa da stampare per visualizzare il nodo ed i figli"
        risultato = '|--'*livello + f"{self._N} {self._LM} {self._mossa}"
        for son in self._figli:
            risultato += '\n' + son.__repr__(livello+1)
        return risultato

    def mosse_valide(self):
        "ciascuna mossa Ã¨ rappresentata dalla coppia: valore da sottrarre, elenco di monete disponibili"
        if self._N == 0:                # se _N == 0
            return []                   # nessuna mossa
        if len(self._LM) == 1:          # se ho solo 1 tipo di moneta (1)
            return [ (1,self._LM) ]     # lo uso e continuo con quella moneta
        if self._LM[0] > self._N:       # se la prima moneta Ã¨ troppo grossa
            return [ (0,self._LM[1:]) ] # la ignoro (sottraggo 0 e continuo senza quella moneta)
        else:
            prima, *resto = self._LM    # altrimenti ho due possibilitÃ 
            return [ (prima,self._LM),  # sottraggo la prima moneta e continuo con lo stesso elenco di monete
                     (0, resto)  ]      # oppure non la sottraggo e smetto di usarla

    def applica_mossa(self, moneta, LM):
        "applicazione di una mossa"
        N1 = self._N - moneta   # detraggo la moneta dal resto
        # aggiungo un nuovo figlio per il nuovo valore e con le monete indicate e mi ricordo che moneta ho sottratto
        self._figli.append(Resto(N1, LM, moneta))   

    def genera(self):
        "Applico tutte le mosse valide e poi lo faccio sui figli generati"
        for M,LM in self.mosse_valide():
            self.applica_mossa(M,LM)
        for figlio in self._figli:
            figlio.genera()

R = Resto(9, [10,5,2,1])
R.genera()
print(R)


# %%% albero di gioco della soluzione dei resti

# definiamo un oggetto AlberoResti
# un nodo del gioco rappresenta la situazione di una soluzione parziale
# - ho ancora N da trasformare in monete
# - ho un gruppo di monete disponibili M
# - ho giÃ  raccolto un gruppo di monete 'resti' come soluzione parziale
# - il nodo ha dei figli se Ã¨ una soluzione parziale (N>0)
# - altrimenti Ã¨ una foglia e contiene una soluzione


# per generare i figli di una posizione di gioco (o configurazione)
# se N == 0 non devo fare altro
# se ho una sola moneta la uso
# se la prima moneta Ã¨ troppo grossa la dimentico
# se la prima moneta Ã¨ OK la uso
# e poi la dimentico (per generare le configurazioni che NON la usano)
# generati i figli passo a generare i loro figli


# %%%% Esempio: N=9 e M=[5,2,1]
A = AlberoResti(9, [5,2,1], [])
A.genera_figli()
print(A)

def foglie(A):
    if A._figli:
        return [ f for son in A._figli for f in foglie(son) ]
    else:
        return [ A._resto ]

print(*foglie(A), sep='\n')

# %%% BYE BYE
# -*- coding: utf-8 -*-

