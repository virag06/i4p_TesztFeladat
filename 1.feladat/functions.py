import string

def kodolo(uzenet, kulcs):

    abc=string.ascii_lowercase

    kodBetu={}
    kodSzam={}
    rejtjelezettUz=""


    for i in range (0,len(abc)):
        kodBetu[abc[i]] = i
        kodSzam[i]=abc[i]

    kodBetu[" "]=26
    kodSzam[26]=" "

    for i in range (0,len(uzenet)):
        eredmeny=kodBetu[uzenet[i]]+kodBetu[kulcs[i]]
        if eredmeny > 26:
            eredmeny=eredmeny%27
        rejtjelezettUz+=kodSzam[eredmeny]

    return rejtjelezettUz
