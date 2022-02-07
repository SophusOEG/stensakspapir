import random


f=0

w=0

for z in range(1,10):
    t1=random.randint(1,3);
    t2=random.randint(1,3);
    if t1==1:
        print("du slog sten")
    if t1==2:
        print("du slog saks")
    if t1==3:
        print("du slog papir")

    if t2==1:
        print("jeg slog sten")
    if t2==2:
        print("jeg slog saks")
    if t2==3:
        print("jeg slog papir")


    if t1==t2:
        print("Det er en ommmer!")
        print("")
    if t1==1 and t2==3:
        print("Jeg vandt!")
        print("")
    if t1==1 and t2==2:
        print("Du vandt!")
        print("")
    if t1==2 and t2==1:
        print("Jeg vandt!")
        print("")
    if t1==2 and t2==3:
        print("Du vandt!")
        print("")
    if t1==3 and t2==1:
        print("Jeg vandt")
        print("")
    if t1==3 and t2==2:
        print("Du vandt!")
        print("")

    
