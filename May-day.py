
print_H=[[" " for i in range(7)]for j in range(7)]
print_A=[[" " for i in range(7)]for j in range(7)]
print_P=[[" " for i in range(7)]for j in range(7)]
print_P=[[" " for i in range(7)]for j in range(7)]
print_Y=[[" " for i in range(7)]for j in range(7)]
print_M=[[" " for i in range(7)]for j in range(7)]
print_D=[[" " for i in range(7)]for j in range(7)]


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

#code for M
for row in range(7):
    for col in range(7):
        if(col==0 or col==6) or (row==col and col<4)or (row==1 and col==5)or(row==2 and col==4):
           print_M[row][col]="*"

#code for A
for row in range(7):
    for col in range(7):
        if((col==0 and row!=0) or (col==6 and row!=0) or (row==3 or row==0) and (col>0 and col<6)):
            print_A[row][col]="*"

#code for Y
for row in range(7):
    for col in range(7):
        if(row==col and col<4)or(col==3 and row>3)or(col==6 and row==0)or(col==5 and row==1)or(col==4 and row==2):
            print_Y[row][col]="*"


#code for D
for row in range(7):
    for col in range(7):
        if((col==0) or (col==6 and row!=0 and row!=6)) or ((row==0 or row ==6) and (col>0 and col<6)):
           print_D[row][col]="*"

#code for A
for row in range(7):
    for col in range(7):
        if((col==0 and row!=0) or (col==6 and row!=0) or (row==3 or row==0) and (col>0 and col<6)):
            print_A[row][col]="*"

#code for Y
for row in range(7):
    for col in range(7):
        if(row==col and col<4)or(col==3 and row>3)or(col==6 and row==0)or(col==5 and row==1)or(col==4 and row==2):
            print_Y[row][col]="*"


print()
print("---------------------------------------------------------------------------------------------------")
print()

for i in range(7):
    for j in range(7):
        print(end=" ")
    print(end=" ")
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
print("-------------------------------------------------------------------------------------------------------")
print()
for i in range(7):
    for j in range(7):
        print(end=" ")
    print(end="                ")
    for j in range(7):
        print(print_M[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end="  ")
    for j in range(7):
        print(print_Y[i][j],end=" ")
    print()
print()
print("----------------------------------------------------------------------------------------------------------")
print()
for i in range(7):
    for j in range(7):
        print(end=" ")
    print(end="                                 ")
    for j in range(7):
        print(print_D[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_Y[i][j],end=" ")
    print()
print()
print("----------------------------------------------------------------------------------------------------------")
print()

    



















                   
