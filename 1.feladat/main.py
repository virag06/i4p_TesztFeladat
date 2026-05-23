import string
from functions import *

uzenet="helloworld"
kulcs="abcdefgijkl"
rejtjelezett="hfnosauzun"


print("A rejtjelezett üzenet: ", kodolo(uzenet,kulcs))
print("Az eredeti üzenet: ", dekodolo(rejtjelezett,kulcs))