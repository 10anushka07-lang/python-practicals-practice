n=int(input("enter the elements you want the fibbonacci series to be calculated till:"))
def fibbonacci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return(fibbonacci(n-1)+fibbonacci(n-2))
print("the fibbonacci series is :")
for i in range(0,n):
    print(fibbonacci(i)) 
