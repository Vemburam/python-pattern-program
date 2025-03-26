
#code for I :
for row in range(7):
    for col in range(7):
        if(col==3 or row==0 or row==6):
            print("*",end="")
        else:
            print(end=" ")
    print()


#code for H (Heart):
for row in range(7):
    for col in range(7):
        if(row==0 and col%3!=0)or(row==1 and col%3==0)or(row-col==3)or(row+col==9)or(col==6 and row==2)or(col==0 and row==2)or(row==1 and col==3):
            print("*",end="")
        else:
            print(end=" ")
    print()

#code for U:
for row in range(7):
    for col in range(7):
        if(col==0 or col==6) and row!=6 or (row==6 and col>0 and col<6):
            print("*",end="")
        else:
            print(end=" ")
    print()



print("######################################################################################################################################################")




print_I=[[" " for i in range (7)]for j in range(7)]
print_H=[[" " for i in range (7)]for j in range(7)]
print_U=[[" " for i in range (7)]for j in range(7)]
def Loveu():
    for row in range(7):
        for col in range(7):
            if(row==0 and col%3!=0)or(row==1 and col%3==0)or(row-col==3)or(row+col==9)or(col==6 and row==2)or(col==0 and row==2)or(row==1 and col==3):
                print_H[row][col]="*"
    for row in range(7):
        for col in range(7):
            if(col==3 or row==0 or row==6):
                print_I[row][col]="*"
    for row in range(7):
        for col in range(7):
            if(col==0 or col==6) and row!=6 or (row==6 and col>0 and col<6):
                print_U[row][col]="*"
print()
print("#####################################################################")
print()
Loveu()
for i in range(7):
    for j in range(7):
        print(print_I[i][j],end=" ")
    print(end="      ")
    for j in range(7):
        print(print_H[i][j],end=" ")
    print(end="        ")
    for j in range(7):
        print(print_U[i][j],end=" ")
    print()
print()
print("#######################################################################")
