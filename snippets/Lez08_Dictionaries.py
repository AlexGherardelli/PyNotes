
# RECAP:
# - dizionari ed istogramma
# velocitÃ  operazioni    

# - sorted e lambda (o funzioni)
# - anagrammi

# TODAY: un altro modo per calcolare se due testi sono anagrammi
# - sort and compare (ovvero strategia della canonicalizzazione)

def isAnagramma(testo, testo1):
    ordinato  = sorted(testo)            # O(N * log N)
    ordinato1 = sorted(testo1)           # O(N * log N)
    return ordinato == ordinato1         # O(N)



# liste di dizionari come modo di rappresentare una tabella 

agenda = [
    {'nome': 'Paperino','cognome':'Paolino',      'telefono':'555-1313',  'indirizzo': 'via dei Peri 113',          'città ': 'Paperopoli'},
    {'nome': 'Gastone', 'cognome':'Paperone',     'telefono':'555-1717',  'indirizzo': 'via dei Baobab 42',         'città ': 'Paperopoli'},
    {'nome': 'Paperon', 'cognome':"de' Paperoni", 'telefono':'555-99999', 'indirizzo': 'colle Papero 1',            'città ': 'Paperopoli'},
    {'nome': 'Archimede','cognome':'Pitagorico',  'telefono':'555-11235', 'indirizzo': 'colle degli Inventori 1',   'città ': 'Paperopoli'},
    {'nome': 'Pietro',  'cognome':'Gambadilegno', 'telefono':'555-66666', 'indirizzo': 'via dei Ladri 13',          'città ': 'Topolinia'},
    {'nome': 'Trudy',   'cognome':'Gambadilegno', 'telefono':'555-66666', 'indirizzo': 'via dei Ladri 13',          'città ': 'Topolinia'},
    {'nome': 'Topolino','cognome':'Mouse',        'telefono':'555-12345', 'indirizzo': 'via degli Investigatori 1', 'città ': 'Topolinia'},
    {'nome': 'Minnie',  'cognome':'Mouse',        'telefono':'555-54321', 'indirizzo': 'via di M.me Curie 1',       'città ': 'Topolinia'},
    {'nome': 'Pippo',   'cognome':"de' Pippis",   'telefono':'555-33333', 'indirizzo': 'via dei Pioppi 1',          'città ': 'Topolinia'},
    ]

# per cercare un numero di telefono (un record) sapendo quale colonna usare e quale valore cerchiamo
def cerca_lineare(ag, colonna, valore):
    # per tutti i record dell'agenda
    for record in ag:
        # se la colonna esiste ed inoltre contiene il valore cercato
        if colonna in record and record[colonna] == valore:
            # torniamo il record
            return record
        # altrimenti
            # torniamo None

# per cercare su piÃ¹ colonne
def cerca_multicolonna_lineare(ag, query):
    # IN : agenda, query: coppie colonna/valore (con un dizionario)
    # OUT: lista dei record che soddisfano tutte le condizioni
    # all'inizio l'elenco di record risultante Ã¨ []
    risultato = []
    # scandiamo l'agenda e per tutti i record
    for record in ag:
        # se corrispondono alla query
        if corrisponde_alla_query(record, query):
            # aggiungo il record all'output
            risultato.append(record)
    # torno l'elenco di record
    return risultato

# per cercare su piÃ¹ colonne con list comprehension
def cerca_multicolonna_lineare_LC(ag, query):
    return [ record for record in ag if corrisponde_alla_query(record, query)    ]

def cerca_multicolonna_lineare_filter(ag, query):
    def c_a_q(record):
        return corrisponde_alla_query(record, query)
    return list(filter( c_a_q, ag ))

def cerca_multicolonna_lineare_lambda(ag, query):
    return list(filter( lambda record: corrisponde_alla_query(record, query) , ag ))


# per ordinare una agenda rispetto ad una colonna
def ordina_rispetto_a_colonna(ag, colonna):
    # usiamo sorted con il parametro key che deve tornare il valore rispetto al quale
    # vogliamo ordinare
    return sorted(ag, key=lambda scheda: scheda[colonna] if colonna in scheda else '' )


# per determinare se un record corrisponde ad una query
def corrisponde_alla_query(record, query):
    # per ciascuna delle coppie colonna : valore cercato
    for colonna, valore in query.items():
        # se NON Ã¨ nel record con quel valore
        if colonna not in record or record[colonna] != valore:
            # torno False
            return False
    # altrimenti torno True
    return True

# per costruire un indice
def crea_indice(agenda, colonna):
    # IN agenda, colonna
    # OUT lista che contiene coppie [valori]: posizioni originali dei record che contengolo quel valore
    # all'inizio il dizionario valori:posizioni Ã¨ vuoto
    indice = {}
    # per ogni record dell'agenda e sua posizione,
    for posizione,record in enumerate(agenda):
        # estraggo dal record il valore per quella colonna
        valore = record[colonna]
        # se il valore Ã¨ nell'indice
        if valore in indice:
            # aggiungo la posizione all'elenco delle posizioni di quel valore
            indice[valore].append(posizione)
        # altrimenti
        else:
            # aggiungo il valore : [posizione]
            indice[valore] = [posizione]
    # ritorno il dizionario valori: posizioni
    return indice


# ricerca in una tabella
# ordinamento in base ad una colonna 
# ordinamento in base ad una colonna passata come argomento
# ordinamento in base a piÃ¹ di una colonna
# costruzione di indici 
# - liste ordinate con ricerca binaria se valori multipli
# - oppure con dizionari se valori unici (oppure dizionari con liste se multipli)
# ricerca tramite indici

##### LunedÃ¬
## files
# - open (bad!)
# - with open (best!)
# - i parametri encoding e mode
# - leggere il file una riga per volta o tutto assieme, pro e contro

## analisi del testo e ricerca
# - estrazione delle parole (rimpiazzando i nonalpha con spazi)
# - costruzione di indici per evitare di dover ricontare le parole
# - eliminazione delle parole piÃ¹ comuni (con frequenze molto/troppo alte, con stopwords)
# - ricerca di file che parlano di piÃ¹ di certe parole
# - importanza delle parole nei file    = tf_i * idf
#    - tf_i  = # presenze / # parole del file                           # frequenza nel file iesimo
#    - idf   = log( # di file / # di file che contengono la parola )    # inverso della frequenza nei documenti

