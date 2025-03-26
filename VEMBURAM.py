#CODE FOR V:
i=0
j=8
for row in range(5):
    for col in range(9):
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
#CODE FOR E:
print()
for row in range(7):
    for col in range(7):
        if(col==0)or(row==0 or row==3 or row==6):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#CODE FOR M:
print()
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col and row>0 and row<4)or(row==1 and col==5)or(row==2 and col==4):
             print("*",end="")
        else:
            print(end=" ")
    print()
print()
#CODE FOR B:
print()
for row in range(7):
    for col in range(7):
        if((col==0 and row!=0) or (col==6 and row!=0 and row!=3 and row!=6)or(row==0 or row==3 or row==6) and (col>0 and col<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#CODE FOR U:
print()
for row in range(7):
    for col in range(7):
        if(col==0 and row!=6) or (col==6 and row!=6) or(row==6 and col>0 and col<6):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#CODE FOR R:
print()
for row in range(7):
    for col in range(7):
        if(col==0 and row!=0) or (row==1 and col==6)or(row==2 and col==6)or(col!=6 and row==0) or (col!=6 and row==3) or(row==col+1 and row>3 and row<=6):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#CODE FOR A:
print()
for row in range(7):
    for col in range(7):
        if(col==0 or col==6) and row!=0 or(row==0 or row==3)and (col>0 and col<6):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
#CODE FOR M:
print()
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col and row>0 and row<4)or(col==5 and row==1)or(col==4 and row==2):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()

print()
print("***********************************************************************************************************************************************************")
print()

strl="VEMBU RAM"
print_V=[[" " for i in range (7)] for j in range (7)]
print_E=[[" " for i in range (7)] for j in range (7)]
print_M=[[" " for i in range (7)] for j in range (7)]
print_B=[[" " for i in range (7)] for j in range (7)]
print_U=[[" " for i in range (7)] for j in range (7)]
print_R=[[" " for i in range (7)] for j in range (7)]
print_A=[[" " for i in range (7)] for j in range (7)]
print_M=[[" " for i in range (7)] for j in range (7)]


#code for V:
for row in range(7):
    for col in range(7):
        if(col==1 and row<4) or(col==5 and row<4)or(col==2 and row==4)or(col==3 and row==6)or(col==4 and row==4):
        #if(row==col and col>=0 and col<4)or(row==0 and col==6)or(row==1 and col==5)or(row==2 and col==4):
            print_V[row][col]="*"
        
#code for E:
for row in range(7):
    for col in range(7):
        if(col==0)or(row==0 or row==3 or row==6):
            print_E[row][col]="*"

#code for M:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col and col>0 and col<3)or (row==0 and col==6)or(row==1 and col==5)or (row==2 and col==4):
            print_M[row][col]="*"

#code for B:
for row in range(7):
    for col in range(7):
        if(col==0 and row!=0) or (col==6 and row!=0 and row!=3 and row!=6)or(row==0 or row==3 or row==6)and(col>0 and col<6):
            print_B[row][col]="*"

#code for U:
for row in range(7):
    for col in range(7):
        if((col==0 and row!=6)or (col==6 and row!=6) or(row==6) and col>0 and col<6):
            print_U[row][col]="*"


#code for R
for row in range(7):
    for col in range(7):
        if(col==0) or (row==1 and col==6)or(row==2 and col==6)or(col!=6 and row==0) or (col!=6 and row==3) or(row==col+1 and row>3 and row<=6):
            print_R[row][col]="*"

#code for A
for row in range(7):
    for col in range(7):
        if(col==0 or col==6) and row!=0 or(row==0 or row==3)and (col>0 and col<6):
            print_A[row][col]="*"

#code for M
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col and row>0 and row<4)or(col==5 and row==1)or(col==4 and row==2):
            print_M[row][col]="*"
print()
print("**************************************************************************************************************************************************************")
print()
for i in range(7):
    for j in range(7):
        print(print_V[i][j],end="")
    print(end=" ")
    for j in range(7):
        print(print_E[i][j],end="")
    print(end=" ")
    for j in range(7):
        print(print_M[i][j],end="")
    print(end=" ")
    for j in range(7):
        print(print_B[i][j],end="")
    print(end=" ")
    for j in range(7):
        print(print_U[i][j],end="")
    print(end="      ")
    for j in range(7):
        print(print_R[i][j],end="")
    print(end=" ")
    for j in range(7):
        print(print_A[i][j],end="")
    print(end=" ")
    for j in range(7):
        print(print_M[i][j],end="")
    print()
print()
print("****************************************************************************************************************************************************************")   


