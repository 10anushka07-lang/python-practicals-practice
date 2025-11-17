lowerbound=int(input("enter the lowerbound:"))
upperbound=int(input("enter the upperbound:"))
sum1=0
for num in range(lowerbound,upperbound+1):
    if num>1:
        primeno=True
        for i in range(2,num):
            if num%i==0:
                primeno=False
                break
        if primeno:
            
            sum1=sum1+num
print("sum of prime no's,",sum1)                
                
