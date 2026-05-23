import string

abc=string.ascii_lowercase

kodBetu={}
kodSzam={}

for i in range (0,len(abc)):
    kodBetu[abc[i]] = i
    kodSzam[i]=abc[i]
kodBetu[" "]=26
kodSzam[26]=" "

def kodolo(uzenet, kulcs):
    rejtjelezettUz=""

    for i in range(0,len(uzenet)):
        eredmeny=kodBetu[uzenet[i]]+kodBetu[kulcs[i]]
        if eredmeny > 26:
            eredmeny=eredmeny%27
        rejtjelezettUz+=kodSzam[eredmeny]

    return rejtjelezettUz

def dekodolo(rejtjelezett,kulcs):
    eredetiUz=""

    for i in range(0,len(rejtjelezett)):
        eredeti=kodBetu[rejtjelezett[i]]-kodBetu[kulcs[i]]
        if eredeti < 0:
            eredeti=eredeti+27
        eredetiUz+=kodSzam[eredeti]

    return eredetiUz