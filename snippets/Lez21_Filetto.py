# %% RECAP
# --- Alberi n-ari
# --- altezza e diametro
# --- Albero che rappresenta una directory ed il suo contenuto

# --- Alberi di gioco
# --- Nodo = configurazione in un certo momento
# --- mossa = regola che permette di generare una nuova configurazione (se possibile)
# --- convergenza = si deve sempre arrivare ad una configurazione in cui non si puÃ² fare mosse

# Esempio: somma di pari+pari e dispari+dispari su una lista di interi
# - ricerca della sequenza di mosse piÃ¹ breve e piÃ¹ lunga
# Esempio: gioco degli anagrammi: date due stringhe A e B una l'anagramma dell'altra 
#          trovare le mosse (scambi di due caratteri) che portano da A a B
# Esempio: gioco del resto con le monete
#          trovare tutti modi di dare il resto (foglie dell'albero)
# ----------------------------------------------------------------------------------
# %% Albero di gioco del TRIS (con 2 giocatori)

# --- Configurazione: scacchiera con simboli 'o', 'x', ' ' (empty cell)
# --- Convergenza: con al massimo 9 mosse la scacchiera Ã¨ piena

# nuovo tipo di errore per comunicare errori del gioco
class FilettoError(Exception):
    pass

class Filetto:
    def __init__(self, configurazione=None):
        "creazione di un nuovo nodo a partire da una data configurazione, rappresentata come matrice 3x3"
        if configurazione is None:                          # se non viene passata
            configurazione = [ [' ']*3 for i in range(3)]   # ne creiamo una vuota
        self._configurazione = configurazione
        self._figli = []                                    # all'inizio non ci sono figli

    def __repr__(self):
        "rappresentazione sotto forma di stringa della tabella"
        return '\n'.join(['|'+ '|'.join(riga)+'|' for riga in self._configurazione ])

# --- Prossimo giocatore
    def prossimo_giocatore(self):
        "si inizia sempre col simbolo 'o' quindi basta contare gli ' ' per sapere a chi tocca"
        conteggio = 0
        for riga in self._configurazione:
            for casella in riga:
                if casella == ' ':
                    conteggio += 1
        if conteggio % 2 == 1:
            return 'o'
        elif conteggio == 0:        # se non ci sono spazi
            return None             # non Ã¨ il turno di nessuno
        else:
            return 'x'

# --- Configurazione vincente per un giocatore G o K (non intendo strategia)
    def vincente(self, giocatore):
        """la configurazione corrente Ã¨ vincente per il giocatore se ci sono 3
        dei suoi simboli in riga, colonna o diagonale"""
        M = self._configurazione
        return ( 
            M[0][0] == M[0][1] == M[0][2] == giocatore  # prima riga
            or 
            M[1][0] == M[1][1] == M[1][2] == giocatore  # seconda riga
            or
            M[2][0] == M[2][1] == M[2][2] == giocatore  # terza riga
            or
            M[0][0] == M[1][0] == M[2][0] == giocatore  # prima colonna
            or 
            M[0][1] == M[1][1] == M[2][1] == giocatore  # seconda colonna
            or
            M[0][2] == M[1][2] == M[2][2] == giocatore  # terza colonna
            or
            M[0][0] == M[1][1] == M[2][2] == giocatore  # diagonale
            or
            M[2][0] == M[1][1] == M[0][2] == giocatore  # antidiagonale
            )

# --- Configurazione che dÃ  patta
    def patta(self):
        "torno True se siamo in una patta (non ci sono caselle libere)"
        return self.prossimo_giocatore() is None

# --- Mosse: inserire il simbolo di turno in una delle caselle vuote
    def applica_mossa(self, x, y, giocatore):
        """data una coordinata x,y provo a vedere se posso inserire il giocatore,
        e costruisco un nuovo figlio con la nuova configurazione"""
        # faccio controlli sul giocatore di turno
        if self.prossimo_giocatore() != giocatore:
            raise FilettoError(f"Non Ã¨ il turno del giocatore {giocatore}")            
        if self._configurazione[y][x] == ' ':       # se la casella Ã¨ libera
            copia = [ riga.copy() for riga in self._configurazione ]    # copio la configurazione
            copia[y][x] = giocatore                 # e ci metto il simbolo alle coordinate x,y
            self._figli.append(Filetto(copia))      # e aggiungo il nuovo nodo ai figli
        else:
            raise FilettoError(f"La casella {x} {y} Ã¨ giÃ  occupata")

# --- elenco delle mosse valide
    def mosse_valide(self):
        """Trovo le mosse valide (ma non ce ne sono se patta o qualcuno ha vinto)"""
        if self.patta():       return []
        if self.vincente('x'): return []
        if self.vincente('o'): return []
        return [ (x,y) for y,riga in enumerate(self._configurazione)
                     for x,casella in enumerate(riga) 
                     if casella == ' ']

# --- generare l'albero di gioco
    def genera(self):
        "Se ci sono mosse valide genero i figli, quindi espando anche i figli"
        mosse = self.mosse_valide()
        pg = self.prossimo_giocatore()
        for x,y in mosse:
            self.applica_mossa(x, y, pg)
        for figlio in self._figli:
            figlio.genera()

# --- Strategia vincente per il giocatore G
# - esiste una mosse per G tale che per tutte le mosse di K si arriva sempre ad una posizione vincente x G
# - se patta NO
# - se vincente per G SI
# - se vincente per K NO
# - se Ã¨ il turno di G basta UNA mossa che porti alla vittoria di G
# - se Ã¨ il turno fi K devono TUTTE portare alla vittoria di G
    def strategia_vincente(self, giocatore):
        "vedo se questa posizione ha una strategia vincente per il giocatore"
        if self.patta():                # no se siamo alla patta
            return False
        if self.vincente(giocatore):    # sÃ¬ se ho giÃ  vinto
            return True
        altro = 'o' if giocatore == 'x' else 'x'
        if self.vincente(altro):        # no se ha vinto l'altro giocatore
            return False
        # altro modo: se non ho figli e ho vinto True else False
        pg = self.prossimo_giocatore()
        if giocatore == pg:             # se tocca a me
            for figlio in self._figli:  # e c'Ã¨ almeno un figlio che Ã¨ vincente posso muovermi lÃ¬ e quindi questa posizione Ã¨ vincente per me
                if figlio.strategia_vincente(giocatore):
                    return True
            else:
                return False            # altrimenti nessuno dei figli Ã¨ vincente, questa posizione non Ã¨ vincente
        else:                           # se invece non Ã¨ il giocatore a dover giocare
            for figlio in self._figli:  # per vincere, nessuna delle scelte dell'avversario deve essere vincente
                if figlio.strategia_vincente(altro):    # se una lo Ã¨, questa posizione NON Ã¨ vincente per me
                    return False
            else:                       # se nessuno dei figli Ã¨ vincente per l'avversario
                return True             # allora io posso vincere da qui


# %%% Esempi

f1 = Filetto([
    ['o', ' ', 'x'],
    [' ', ' ', 'o'],
    ['x', ' ', 'o'],    
    ])
#print(f1.vincente('x'))
#print(f1.prossimo_giocatore())
#print(f1.patta())
#f1.applica_mossa(1, 0, 'x')
f1.genera()
print(f1.strategia_vincente('x'))

# Ottimizzazione: Equivalenza tra configurazioni (per ridurre le dimensioni dell'albero da creare)

# %% semplificazione di espressioni algebriche (proseguiamo lunedÃ¬)

class EspressioneError(Exception):
    pass

# consideriamo solo espressioni algebriche con solo operatori binari (*+./^)
# le foglie contengono valori (interi per semplificare) oppure nomi di variabili
# senza precedenza tra operatori: ogni operazione Ã¨ racchiusa tra parentesi

# descrizione della sintassi
# espressione ::= numero
# espressione ::= variabile
# espressione ::= '(' espressione operatore espressione ')'
# operatore   ::= '*' | '+' | '-' | '/' | '^'
# variabile   ::= *un carattere alfabetico*
# numero      ::= una sequenza di *cifre*

class Numero(Espressione):
    '''
    Un numero contiene un valore numerico
    '''
    def __init__(self, valore):
        self._valore = valore

    # calcolo della espressione algebrica da un albero (con variabili)
    def calcola(self, environment):
        "il suo valore Ã¨ proprio l'attributo self._valore"
        return self._valore

    # disegno cell'espressione con la turtle
    def draw(self, tartaruga):
        # ne stampo il valore centrato poco piÃ¹ in basso
        x,y = tartaruga.position()
        tartaruga.goto(x,y-30)
        tartaruga.pendown()
        tartaruga.write(self._valore, align='center', font=('Arial',20,'bold'))
        tartaruga.penup()
        tartaruga.goto(x,y)

    # --- stampa della espressione algebrica da un albero
    def __repr__(self):
        "il testo che rappresenta questo oggetto non Ã¨ altro che il valore come stringa"
        return str(self._valore)

class Variabile(Espressione):
    def __init__(self, nome):
        "una variabile ha un nome (stringa)"
        self._nome = nome
        
    # calcolo del valore della variabile
    def calcola(self, environment):
        "dato un dizionario { nome -> valore }, una variabile ha il valore che nel dizionario corrisponde al suo nome"
        try:
            return environment[self._nome]
        except KeyError:
            raise EspressioneError(f"La variabile {self._nome} non Ã¨ presente nell'environment")

    def draw(self, tartaruga):
        "disegno il nome della variabile centrato"
        x,y = tartaruga.position()
        tartaruga.goto(x,y-30)
        tartaruga.pendown()
        tartaruga.write(self._nome, align='center', font=('Arial',20,'bold'))
        tartaruga.penup()
        tartaruga.goto(x,y)

    # --- stampa della espressione algebrica da un albero
    def __repr__(self):
        "come stringa la variabile Ã¨ rappresentata dal suo nome"
        return self._nome

class Espressione:
    def __init__(self, argomento1, operatore, argomento2):
        "una Espressione ha sempre due argomenti ed un operatore (+-*/^)"
        self._operatore = operatore
        self._argomento1 = argomento1
        self._argomento2 = argomento2

    # calcolo della espressione algebrica da un albero (con variabili)
    # environment Ã¨ un dizionario { variabile -> valore } che permette di calcolare
    # l'espressione per certi valori delle variabili
    def calcola(self, environment):
        "per calcolare il valore di una espressione prima calcolo i due argomenti e poi applico l'operatore"
        arg1 = self._argomento1.calcola(environment)    # passo l'environment alle due sottoespressioni
        arg2 = self._argomento2.calcola(environment)    # che potrebbero contenere variabili
        if self._operatore == '+':
            return arg1 + arg2
        if self._operatore == '-':
            return arg1 - arg2
        if self._operatore == '*':
            return arg1 * arg2
        if self._operatore == '/':
            return arg1 / arg2
        if self._operatore == '^':
            return arg1 ** arg2

#             +
#          /     \
#   (((2*3)+5)+(7/x))

#  |----v----|  larghezza espressione
#   12345
#   12
#  |-^-|--^--|  centri delle sottoespressioni

    def draw(self, tartaruga):
        "disegno l'albero binario che corrisponde alla espressione"
        tartaruga.pendown()
        tartaruga.write(self._operatore, align='center', font=('Arial',20, 'bold'))     # prima l'operatore
        larghezza1 = len(str(self._argomento1))*10  # larghezza del primo operando (in caratteri * 10)
        larghezza2 = len(str(self._argomento2))*10  # larghezza del secondo operando
        larghezza  = len(str(self))*10              # larghezza di tutto l'albero
        centro  = larghezza/2                       # posizione della radice
        centro1 = larghezza1/2                      # centro del sottoalbero arg1
        centro2 = larghezza2/2                      # centro del sottoalbero arg2
        x, y = tartaruga.position()                 # data la posizione della radice
        origine = x - centro                        # bordo sinistro dell'albero
        tartaruga.pendown()
        tartaruga.goto(origine + centro1, y -50)    # il sottoalbero SX sta centro1 dal bordo sinistro 
        tartaruga.penup()
        self._argomento1.draw(tartaruga)            # lo disegno
        tartaruga.goto(x , y)
        tartaruga.pendown()
        tartaruga.goto(origine + larghezza - centro2, y -50) # il destro sta centro2 dal bordo destro
        tartaruga.penup()
        self._argomento2.draw(tartaruga)            # lo disegno
        tartaruga.goto(x , y)                       # e torno sulla radice

    # --- stampa della espressione algebrica da un albero
    def __repr__(self):
        # qua ci sono 2 chiamate ricorsive implicite a __repr__ per inserire gli argomenti nella stringa
        return f"({self._argomento1} {self._operatore} {self._argomento2})"

    #################################################################################
    #################################################################################
    #################################################################################
    ############        LunedÃ¬ continuiamo da qui                   #################
    #################################################################################
    #################################################################################
    #################################################################################

    def __eq__(self, other):
        return (isinstance(other, Espressione) and
            self._operatore == other._operatore 
            and
            self._argomento1 == other._argomento1
            and 
            self._argomento2 == other._argomento2
            )


    def semplifica(self):
        # 1 * X = X
        if self._argomento1 == Numero(1) and self._operando == '*':
            return self._argomento2
        # 0 * X = 0
        if self._argomento1 == Numero(0) and self._operando == '*':
            return Numero(0)

        # X^1 = X
        if self._argomento2 == Numero(1) and self._operando == '^':
            return self._argomento1
        # X^0 = 1
        if self._argomento2 == Numero(0) and self._operando == '^':
            return Numero(1)

        # 0 + X = X
        if self._argomento1 == Numero(0) and self._operando == '+':
            return self._argomento2

        # X - 0 = X
        if self._argomento2 == Numero(0) and self._operando == '-':
            return self._argomento1            
        # X - X = 0
        if self._argomento2 == self._argomento1 and self._operando == '-':
            return Numero(0)

        # X / 1 = X
        if self._argomento2 == Numero(1) and self._operando == '/':
            return self._argomento1            



# %%%% Esempio di albero

n1 = Numero(42)
n2 = Numero(34)
n3 = Numero(-300)
n4 = Numero(-999)
v1 = Variabile('x')
v2 = Variabile('y')
e1 = Espressione( n1, '*', v1 )  # (42 * x)
e2 = Espressione( n2, '+', v2 )  # (34 * y)
e3 = Espressione( n3, '/', n4 )  # (-300 / -999)
e4 = Espressione( e1, '-', e2 )  # ((42 * x) - (34 * y))
e5 = Espressione( e4, '+', e3 )  # (((42 * x) - (34 * y)) + (-300 / -999))

print(e5)

env = { 'x': 10, 'y': 20, 'z': 3  }

print(e5.calcola(env))

# %%% costruzione dell'albero da una espressione algebrica (parser)

# la funzione analizza la parte iniziale della stringa, riconoscendo l'espressione
# e la torna assieme alla parte di testo che ancoraa non Ã¨ stata esaminata

def analizza(stringa):    
    # FIXME: Prima di chiamare analizza conviene togliere eventuali spazi con replace
    primo, *resto = stringa         # prendo il primo carattere e lascio in resto i rimanenti
    if primo.isdecimal():           # se Ã¨ una cifra
        # torno un Numero con tutte le cifre che trovo
        valore = primo              # concateno le cifre
        while resto and resto[0].isdecimal():   # se ce ne sono ancora
            valore += resto.pop(0)              # tolgo la prima cifra
        # quando non ne trovo piÃ¹
        return Numero(int(valore)), resto       # costruisco il numero e torno il resto del testo non analizzato 
    if primo == '(':                # se invece il primo carattere Ã¨ una '(' devo riconoscere una espressione
        # torno una espressione cercando: espressione operatore espressione ')'
        arg1, resto1 = analizza(resto)          # con una chiamata ricorsiva riconosco la prima espressione
        operatore, *resto2 = resto1             # nel resto del testo il primo carattere Ã¨ l'operatore
        if operatore not in '*+-/^':            # se Ã¨ sbagliato lancio un errore
            raise EspressioneError("mi aspettavo un operatore '*+-/^' invece di "+operatore)
        arg2, resto3 = analizza(resto2)         # analizzo il testo dopo l'operatore
        if resto3[0] != ')':                    # e subito dopo mi aspetto di trovare la ')'
            raise EspressioneError("mi aspettavo una ) e invece ho trovato una "+resto3[0])
        # se tutto Ã¨ andato bene posso costruire l'espressione e tornare il testo che segue la ')'
        return Espressione(arg1, operatore, arg2), resto3[1:]
    else:                                       # altrimenti dovrebbe essere una variabile (con un solo carattere)
        # torno una Variabile
        return Variabile(primo), resto          # la costruisco e torno il resto dei caratteri che la seguono

# %%% Esempi

E, resto = analizza('((x+34)-(y/(7^z)))')

print(E)

print(E.calcola(env))

# %%% visualizzazione dell'abero con la turtle

import turtle
t = turtle.Turtle()

t.reset()

#E.draw(t)

E1,_ = analizza("((((3+y)-12345678)+y)*12345678)")
E1.draw(t)

# %%% semplificazione


# - equivalenza (e operatori commutativi)
# - assorbimento su * + - /
# - esiste una forma "canonica" della formula? (aiuta nei controlli e diminuisce il nÂ° di regole)

# - singolo passaggio di semplificazione
# - applicazione ricorsiva della semplificazione partendo dalle foglie a salire

# %% derivazione di espressioni algebriche

# - regole di derivazione come trasformazioni della espressione

# %% BYE BYE
