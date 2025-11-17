str1=str(input("enter a string:"))
str2=str(input("enter second string:"))
print("strings before swapping",str1,str2)
str1=str1+str2
str2=str1[0:len(str1)-len(str2)]
str1=str1[len(str2)::]
print("strings before swapping",str1,str2)
