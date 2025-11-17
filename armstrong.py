num=int(input("enter the value of num:"))
order=len(str(num))
sum1=0
temp=num
while temp>0:
    digit=temp%10
    sum1=sum1+(digit**order)
    temp=temp//10
if num==sum1:
    print(num,"is an armstrong no")
else:
    print("num is not an armstrong no") 
