import threading
import time
import random as r


coordinates=[100,100,100]
randOm_or_fIxed=0 ## Set it to 0 for random flying/ 1 for keeping around a fized point/anything else for error 

def gorandom():
    global coordinates
    print("watch me go random")
    while(True):
        ranx=r.randint(-10,10)
        rany=r.randint(-10,10)
        if(coordinates[2] <= 20):
            ranz=r.randint(0,10)
        elif(coordinates[2] > 20):
            ranz=r.randint(-10,10)
        coordinates[0]=coordinates[0]+ranx
        coordinates[1]=coordinates[1]+rany
        coordinates[2]=coordinates[2]+ranz
        print(coordinates)
        time.sleep(0.5)


def gocorona():
    global coordinates
    print("watch me loiter around ",str(coordinates))
    initx=coordinates[0]
    inity=coordinates[1]
    initz=coordinates[2]
    while(True):
        if(coordinates[0] <= initx):
            ranx=r.randint(0,10)
        elif(coordinates[0] > initx):
            ranx=r.randint(-10,0)
        if(coordinates[1] <= inity):
            rany=r.randint(0,10)
        elif(coordinates[1] > inity):
            rany=r.randint(-10,0)
        if(coordinates[2] <= initz):
            ranz=r.randint(0,10)
        elif(coordinates[2] > initz):
            ranz=r.randint(-10,0)
        
        coordinates[0]=coordinates[0]+ranx
        coordinates[1]=coordinates[1]+rany
        coordinates[2]=coordinates[2]+ranz
        print(coordinates)
        time.sleep(0.5)

print(coordinates)
if randOm_or_fIxed=0:
    lol=threading.Thread(target=gorandom)
elif randOm_or_fIxed=1:
    lol=threading.Thread(target=gocorona)
lol.start()
