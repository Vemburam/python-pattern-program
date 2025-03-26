#A
for row in range(7):
    for col in range(5):
        if(col==0 and row!=0) or (col==4 and row!=0)or((row==0 or row==3) and (col>0 and col<4)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()

#B
for row in range(7):
    for col in range(5):
        if(col==0 and row!=0) or (col==4 and row!=0 and row!=6 and row!=3)or((row==0 or row==3 or row==6) and (col>0 and col<4)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()

#C
for row in range(7):
    for col in range(5):
        if(col==0 and row!=0 and row!=6) or ((row==0 or row==6) and (col>0)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()

#D
for row in range(7):
    for col in range(5):
        if((col==0) or (col==4 and row!=0 and row!=6)) or ((row==0 or row ==6) and (col>0 and col<4)):
           print("*",end="")
        else:
            print(end=" ")
    print()
print()

#E
for row in range(7):
    for col in range(5):
        if(col==0)or(row==0 or row==3 or row==6)and (col>0 and col<4):
            print("*",end="")
        else:
            print(end="")
    print()
print()

#F
for row in range(7):
    for col in range(5):
        if(col==0)or(row==0 or row==3)and(col>0 and col<4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#G
for row in range(7):
    for col in range(7):
        if(col==0)or(col==3 and row!=1 and row!=2)or(col==5 and row!=1 and row!=2) or(row==0 and col>0 and col<=4 )or (row==6 and col>0 and col<4)or(row==3 and col==4)or(row==3 and col==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#H
for row in range(7):
    for col in range(5):
        if(col==0 or col==4) or ((row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#I
for row in range(7):
    for col in range(5):
        if(col==2)or(row==0 or row==6)or(row==0 or row==6)and(col>0 and col<4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#J
for row in range(7):
    for col in range(5):
        if(col==2)or(row==0 or row==6 and col<2)or(row==0 or row==6 and col<2)and(col>0 and col<4)or(col==0 and row==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#K
i=0
j=4
for row in range(7):
    for col in range(5):
        if(col==0)or((row==col+2)and(col>1)):
            print("*", end="")
        elif((row==i and col==j)and (col>=1)):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()
print()

#L
for row in range(7):
    for col in range(5):
        if(col==0) or (row==6) and (col>0 or col<4):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()

#M
for row in range(7):
    for col in range(7):
        if(col==0 or col==6) or (row==col and col<4)or (row==1 and col==5)or(row==2 and col==4):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()

#N
for row in range(7):
    for col in range(7):
        if(col==0 or col==6) or (row==col and col<6):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()

#O
for row in range (7):
    for col in range(5):
        if((col==0 and row!=0 and row!=6) or (col==4 and row!=0 and row!=6))or(row==0 or row==6)and (col>0 and col<4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#P
for row in range(7):
    for col in range(7):
        if(col==0)or((row==0 and col!=6) or (row==3 and col!=6))or(row==1 and col==6)or(row==2 and col==6):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#Q
for row in range(7):
    for col in range(7):
        if(col==0 or col==5)or(row==0 and col!=6) or (row==6 and col!=6)or (col==3 and row==4)or(col==4 and row==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#R
for row in range(7):
    for col in range(5):
        if col==0 or (row==1 and col==4) or (row==2 and col==4) or (row==0 and col!=4 or row==3 and col!=4) or (row==col+2):
           print("*",end="")
        else:
            print(end=" ")
    print()
print()

#S
for row in range(7):
    for col in range(7):
        if(row==0 or row==3 or row==6) and (col>0 and col<6) or (col==0 and(row>0 and row<3)) or (col==6 and (row>3 and row<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#T
for row in range(7):
    for col in range(7):
        if(col==3 or row==0):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#U
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)and row!=6 or (row==6 and (col>0 and col<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#V
i=0
j=10
for row in range(6):
    for col in range(11):
        if(row==col):
            print("*",end="")
        elif(row==i and col==j):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()
print()

#W
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(col==row and col>=3 and col<6)or(col==1 and row==5)or (col==2 and row==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#X
i=0
j=6
for row in range(7):
    for col in range(7):
        if(row==i and col==j):
            print("*",end="")
            i=i+1
            j=j-1
        elif(row==col):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#Y
for row in range(7):
    for col in range(7):
        if(row==col and row<3)or (col==3 and row>=3) or (col==6 and row==0)or(col==5 and row==1)or (col==4 and row==2):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

#Z
i=0
j=6
for row in range(7):
    for col in range(7):
        if(row==i and col==j):
            print("*",end="")
            i=i+1
            j=j-1
        elif(row==0 or row==6):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

