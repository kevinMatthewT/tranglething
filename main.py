f=eval(input("Enter number of rows:"))
for i in range(1,f+1):
    for j in range(1,f+1-i):
        print(" ",end="")
    print("*"*i)