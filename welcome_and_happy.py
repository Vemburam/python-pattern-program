str=("WELCOME")
str=("HAPPY")
print_W=[[" " for i in range(7)]for j in range(7)]
print_E=[[" " for i in range(7)]for j in range(7)]
print_L=[[" " for i in range(7)]for j in range(7)]
print_C=[[" " for i in range(7)]for j in range(7)]
print_O=[[" " for i in range(7)]for j in range(7)]
print_M=[[" " for i in range(7)]for j in range(7)]
print_E=[[" " for i in range(7)]for j in range(7)]

print_H=[[" " for i in range(7)]for j in range(7)]
print_A=[[" " for i in range(7)]for j in range(7)]
print_P=[[" " for i in range(7)]for j in range(7)]
print_P=[[" " for i in range(7)]for j in range(7)]
print_Y=[[" " for i in range(7)]for j in range(7)]

#code for W
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col and col>=3)or(col==1 and row==5)or(col==2 and row==4):
            print_W[row][col]="*"
#code for E
for row in range(7):
    for col in range(7):
        if(col==0)or(row==0 or row==3 or row==6):
            print_E[row][col]="*"
#code for L
for row in range(7):
    for col in range(7):
        if(col==0)or (row==6) and (col>0 or col<6):
            print_L[row][col]="*"

#code for C
for row in range(7):
    for col in range(7):
         if(col==0 and row!=0 and row!=6) or ((row==0 or row==6) and (col>0)):
            print_C[row][col]="*"

#code for O
for row in range(7):
    for col in range(7):
        if((col==0 and row!=0 and row!=6) or (col==6 and row!=0 and row!=6)or(row==0 or row==6)and(col>0 and col<6)):
            print_O[row][col]="*"

#code for M
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col and col<4)or(row==1 and col==5)or(row==2 and col==4):
            print_M[row][col]="*"
#code for E
for row in range(7):
    for col in range(7):
        if(col==0)or(row==0 or row==3 or row==6):
            print_E[row][col]="*"

#code for H
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==3):
            print_H[row][col]="*"

#code for A
for row in range(7):
    for col in range(7):
        if((col==0 and row!=0) or (col==6 and row!=0) or (row==3 or row==0) and (col>0 and col<6)):
            print_A[row][col]="*"

#code for P
for row in range(7):
    for col in range(7):
       if(col==0)or((row==0 and col!=6) or (row==3 and col!=6))or(row==1 and col==6)or(row==2 and col==6):
            print_P[row][col]="*"
#code for P
for row in range(7):
    for col in range(7):
        if(col==0)or((row==0 and col!=6) or (row==3 and col!=6))or(row==1 and col==6)or(row==2 and col==6):
            print_P[row][col]="*"

#code for Y
for row in range(7):
    for col in range(7):
        if(row==col and col<4)or(col==3 and row>3)or(col==6 and row==0)or(col==5 and row==1)or(col==4 and row==2):
            print_Y[row][col]="*"


#for output
print()
print("********************************************************************************************************************************************************************************************************")
print()
for i in range(7):
    for j in range(7):
        print(print_W[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_E[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_L[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_C[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_O[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_M[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_E[i][j],end=" ")
    print(end="      |      ")
    for j in range(7):
        print(print_H[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_P[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_P[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_Y[i][j],end=" ")
    print()

print()
print("*********************************************************************************************************************************************************************************************************")
print()



        
        





















        
    
