import random
import time

#from BubbleSort import List

#Funktio randomisoidun listan luontiin:
def CreateList(i):
    RandomizedList = []
    for l in range(i):
        n = random.randint(1, 100)
        RandomizedList.append(n)
    return RandomizedList
        
       
#Funktio listan numeroiden lajitteluun BubbleSort algoritmilla:
def BubbleSort(List):
    n = len(List)
    switch = False
    
    #Käydään listan elementit läpi
    for j in range(n-1):
        for i in range(n-j-1):
            #Vaihdetaan elementtien paikat, jos tarkasteltava elementti on isompi kuin seuraava elementti:
            if (List[i] > List[i + 1]):
                switch = True
                List[i], List[i + 1] = List[i + 1], List[i]
                #Tulostetaan lista jokaisen iteraation jälkeen.
                #print(List)
        #Jos listalle ei tarvitse tehdä yhtään vaihtoa, niin poistutaan loopista suoraan.
        if not switch:
            return

#Luodaan lajiteltava lista ja tulostetaan se käyttäjälle: 
List = CreateList(10000)
print("Randomisoitu lista on:\n" + str(List))

#Aloitetaan ajastin BubbleSort algoritmille:
StartTime = time.time() 

#Lajitellaan lista ja tulostetaan se käyttäjälle kuluneen ajan kanssa:
BubbleSort(List)

print("\nLajiteltu lista on:\n" + str(List))
print("Kulunut aika:", round(time.time()-StartTime, 2), "s.")
