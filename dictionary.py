dict1={"Argentina": "Messi","Portugal":"Ronaldo","Croatia":"Modric","Brazil":"Neymar"}

while True:
    print("---MENU---")
    print("1. Items")
    print("2. Keys")
    print("3. Pop")
    print("4. Values")
    print("5. Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("Items in dictionary: ",dict1.items())
    elif choice==2:
        print("Keys in dictionary: ", dict1.keys())
    elif choice==3:
        key2=input("enter the key you want to pop: ")
        popped_key=dict1.pop(key2)
        print("Popped Eelement: ", popped_key)
        print("Dictionary after pop : ", dict1)
    elif choice==4:
        print("Values pf the Dictionary: ",dict1.values())
    elif choice==5:
        print("Thank you")
        break
    else:
        print("Invalid Input")