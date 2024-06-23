n = int(input("enter: "))
flag=0
for i in range(2,n):
    if n>0:
        for j in range(2,(i//2)+1):
            if i%j==0:
                flag=1
        if flag==1:
            print(i," is not prime")
        else:
            print(i," is prime ")
    else:
        print("not ")
    #flag=0
