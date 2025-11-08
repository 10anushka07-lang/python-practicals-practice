
tuple2=("anushka","riddhi")
while 1:
    print("tuple methods")
    print("1.find index of a value:")
    print("2.count the occurence of an element:")
    print("3.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
       a=tuple2.index("riddhi")
       print(a)
       
    elif ch==2:
        d=tuple2.count("anushka")
        print(d)
        
        