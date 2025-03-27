#Separate PYTHON Letters:

#Code for P:
for row in range(7):
    for col in range(7):
        if(col==0)or(row==0 and col!=6) or (row==3 and col!=6)or((row==1 or row==2) and col==6):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

#for value Y:
for row in range(7):
    for col in range(7):
        if(row==col and col>=0 and col<4)or(col==3 and row>3)or(row==0 and col==6)or(row==1 and col==5)or(row==2 and col==4):
             print("*",end="")
        else:
            print(" ",end="")
    print()
print()

#for value T:
for row in range(7):
    for col in range(7):
        if(col==3)or(row==0):
             print("*",end="")
        else:
            print(" ",end="")
    print()
print()

#for value H:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==3):
             print("*",end="")
        else:
            print(" ",end="")
    print()
print()

#for value O:
for row in range(7):
    for col in range(7):
        if(col==0 and row!=0 and row!=6) or (col==6 and row!=0 and row!=6)or(row==0 or row==6)and(col>0 and col<6):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

#for value N:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

print("################################################################################################")
print()

strl="PYTHON"

print_P=[[" " for i in range(7)]for j in range(7)]
print_Y=[[" " for i in range(7)]for j in range(7)]
print_T=[[" " for i in range(7)]for j in range(7)]
print_H=[[" " for i in range(7)]for j in range(7)]
print_O=[[" " for i in range(7)]for j in range(7)]
print_N=[[" " for i in range(7)]for j in range(7)]

#for value P:
for row in range(7):
    for col in range(7):
        if(col==0)or(row==0 and col!=6) or (row==3 and col!=6)or((row==1 or row==2) and col==6):
            print_P[row][col]="*"

#for value Y:
for row in range(7):
    for col in range(7):
        if(row==col and col>=0 and col<4)or(col==3 and row>3)or(row==0 and col==6)or(row==1 and col==5)or(row==2 and col==4):
            print_Y[row][col]="*"

#for value T:
for row in range(7):
    for col in range(7):
        if(col==3)or(row==0):
            print_T[row][col]="*"
            
#for value H:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==3):
            print_H[row][col]="*"

#for value O:
for row in range(7):
    for col in range(7):
        if(col==0 and row!=0 and row!=6) or (col==6 and row!=0 and row!=6)or(row==0 or row==6)and(col>0 and col<6):
            print_O[row][col]="*"


#for value N:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col):
            print_N[row][col]="*"





#Code for OUTPUT:
print("----------------------------------------------------------------------------------------------------")
print()
for i in range(7):
    for j in range(7):
        print(print_P[i][j],end=" ")
    print(end="   ")
    for j in range(7):
        print(print_Y[i][j],end=" ")
    print(end="   ")
    for j in range(7):
        print(print_T[i][j],end=" ")
    print(end="   ")
    for j in range(7):
        print(print_H[i][j],end=" ")
    print(end="   ")
    for j in range(7):
        print(print_O[i][j],end=" ")
    print(end="   ")
    for j in range(7):
        print(print_N[i][j],end=" ")
    print()
print()
print("----------------------------------------------------------------------------------------------------")       
