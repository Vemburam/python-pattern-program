str1="Happy"
str2="Ramadan"
str3="Mubarak"

print_H=[[" "for i in range(7)]for j in range(7)]
print_A=[[" "for i in range(7)]for j in range(7)]
print_P=[[" "for i in range(7)]for j in range(7)]
print_P=[[" "for i in range(7)]for j in range(7)]
print_Y=[[" "for i in range(7)]for j in range(7)]
print_R=[[" "for i in range(7)]for j in range(7)]
print_A=[[" "for i in range(7)]for j in range(7)]
print_M=[[" "for i in range(7)]for j in range(7)]
print_A=[[" "for i in range(7)]for j in range(7)]
print_D=[[" "for i in range(7)]for j in range(7)]
print_A=[[" "for i in range(7)]for j in range(7)]
print_N=[[" "for i in range(7)]for j in range(7)]
print_M=[[" "for i in range(7)]for j in range(7)]
print_U=[[" "for i in range(7)]for j in range(7)]
print_B=[[" "for i in range(7)]for j in range(7)]
print_A=[[" "for i in range(7)]for j in range(7)]
print_R=[[" "for i in range(7)]for j in range(7)]
print_A=[[" "for i in range(7)]for j in range(7)]
print_K=[[" "for i in range(7)]for j in range(7)]



#CODE FOR H:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==3):
            print_H[row][col]="*"


#CODE FOR A:
for row in range(7):
    for col in range(7):
        if((col==0 and row!=0) or (col==6 and row!=0) or (row==3 or row==0) and (col>0 and col<6)):
            print_A[row][col]="*"

#CODE FOR P:
for row in range(7):
    for col in range(7):
       if(col==0)or((row==0 and col!=6) or (row==3 and col!=6))or(row==1 and col==6)or(row==2 and col==6):
            print_P[row][col]="*"
#CODE FOR P:
for row in range(7):
    for col in range(7):
        if(col==0)or((row==0 and col!=6) or (row==3 and col!=6))or(row==1 and col==6)or(row==2 and col==6):
            print_P[row][col]="*"

#CODE FOR Y:
for row in range(7):
    for col in range(7):
        if(row==col and col<4)or(col==3 and row>3)or(col==6 and row==0)or(col==5 and row==1)or(col==4 and row==2):
            print_Y[row][col]="*"
            
#FOR CODE R:
for row in range(7):
    for col in range(7):
        if(col==0) or(row==0 and col!=0 and col!=6) or (row==3)or(col==6 and row==1)or(col==6 and row==2)or(row==col+1 and col>2):
            print_R[row][col]="*"

#FOR CODE A:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)and row!=0 or(row==0 or row==3)and (col>0 and col<6):
            print_A[row][col]="*"
            
#FOR CODE M:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col and col<4)or(row==1 and col==5)or(row==2 and col==4):
            print_M[row][col]="*"

#FOR CODE A:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)and row!=0 or(row==0 or row==3)and (col>0 and col<6):
            print_A[row][col]="*"

#FOR CODE D:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6 and row!=0 and row!=6)or(row==0 or row==6)and (col>0 and col<6):
            print_D[row][col]="*"
            
#FOR CODE A:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)and row!=0 or(row==0 or row==3)and (col>0 and col<6):
            print_A[row][col]="*"

#FOR CODE N:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or(row==col):
            print_N[row][col]=" "

#FOR CODE M:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or (row==col and row<4)or(row==1 and col==5)or(row==2 and col==4):
            print_M[row][col]="*"

#FOR CODE U:
for row in range(7):
    for col in range(7):
        if(col==0 and row!=6) or (col==6 and row!=6)or(row==6)and(col>0 and col<6):
            print_U[row][col]="*"
            
#FOR CODE B:
for row in range(7):
    for col in range(7):
        if(col==0 and row!=0)or (col==6 and row!=0 and row!=3 and row!=6)or (row==0 or row==3 or row==6)and (col>0 and col<6):
            print_B[row][col]="*"

#FOR CODE A:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)and row!=0 or(row==0 or row==3)and (col>0 and col<6):
            print_A[row][col]="*"

#FOR CODE R:
for row in range(7):
    for col in range(7):
        if(col==0) or(row==0 and col!=0 and col!=6) or (row==3)or(col==6 and row==1)or(col==6 and row==2)or(row==col+1 and col>2):
            print_R[row][col]="*"

#FOR CODE A:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6)and row!=0 or(row==0 or row==3)and (col>0 and col<6):
            print_A[row][col]="*"

#FOR CODE K:
for row in range(7):
    for col in range(7):
        if(col==2)or(row==col and col>2)or(row==0 and col==6)or(row==1 and col==5)or (row==2 and col ==4)or (row==3 and col==3):
            print_K[row][col]="*"
            
# OUTPUT:

print()
print("----------------------------------------------------------------------------------------------------------------------------------------")
print()
for i in range(7):
    for j in range(7):
        print(end=" ")
    print(end="  ")
    for j in range(7):
        print(print_H[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_P[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_P[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_Y[i][j],end=" ")
    print()
print()
print("-------------------------------------------------------------------------------------------------------------------------------------")
print()
for i in range(7):
    for j in range(7):
        print(end=" ")
    print(end="                    ")
    for j in range(7):
        print(print_R[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_M[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_D[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_N[i][j],end=" ")
    print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()

for i in range(7):
    for j in range(7):
        print(end=" ")
    print(end="                             ")
    for j in range(7):
        print(print_M[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_U[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_B[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_R[i][j],end=" ")
    print(end=" ")
    for j in range(7):
        print(print_A[i][j],end=" ")
    print(end="")
    for j in range(7):
        print(print_K[i][j],end=" ")
    print()
print()
print()
print("----------------------------------------------------------------------------------------------------------------------------------------")
print()
    















        
