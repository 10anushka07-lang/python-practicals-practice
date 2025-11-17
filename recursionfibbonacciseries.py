def fibbonacci(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return (fibbonacci(n-1)+fibbonacci(n-2))
n=int(input("\n enter the value of n"))
print("\n fibbonacci series is:")
for i in range(0,n):
    print(fibbonacci(i),end="")    
    
        