list1=[]
tuple1=()
tuple2=("anushka","riddhi")
while 1:
    print("tuple methods")
    print("1.create a tuple")
    print("2.display the tuple")
    print("3.access an element by index ")
    print("4.count occurence of an element ")
    print("5.find index of a value")
    print("6.concatenate another tuple")
    print("7.repeat the tuple")
    print("8.length of tuple")
    print("9.slice the tuple")
    print("10.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        n=int(input("enter the no.of elements you want in the tuple:"))
        for i in range(n):
            a=int(input("enter the element"))
            list1.append(a)
            tuple1=tuple(list1)
    elif ch == 2:
        print("Tuple contents:", tuple1)
    elif ch==3:
        element=(input("enter the element whose index you want :"))
                