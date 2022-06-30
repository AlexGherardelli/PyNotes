def es5(tree):
    # inserisci qui il tuo codice
    d={}
    for x in tree.f:
        d1=es5(x)
        for x in d1:
            if x in d: 
                d[x]=d[x] | d1[x]
            else:
                d[x]=d1[x]
    y=len(tree.f)
    if y in d:
        d[y]=d[y]|  {tree.id}
    else: d[y]=  {tree.id}        
    return d 