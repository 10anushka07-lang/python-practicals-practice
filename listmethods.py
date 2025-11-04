a=list(input("enter the list:"))
while(1):
    print("the menu")
    print("1.append an element into the list:")
    print("2.insert an element into the list:")
    print("3.append a list to a given list:")
    print("4.modify an existing element into the list:")
    print("5.delete an existing element from the list:")
    print("6.delete an existing element from it's position:")
    print("7.sort the list in ascending order:")
    print("8.display the list:")
    print("9.exit")
    ch=int(input("enter your choice:"))
    if(ch==1):
        print("1.append an element into the list:")
        element=(input("enter the element you want to append:"))
        a.append(element)
      
    elif(ch==2):
        print("2.insert an element into the list:")
        index=int(input("enter the index you want the element to be inserted at :"))
        element=(input("enter the element you want to be inserted:"))
        a.insert(index,element)
    
    elif(ch==3):
        print("3.append a list to a given list:")
        list=list(input("enter the list you want to append:"))
        a.extend(list)
    elif(ch==4):
        print("4.modify an existing element into the list:")
        index=int(input("enter the index of the element you want to update:"))
        value=(input("enter the value you want to insert: "))
        a[index]=value
    elif(ch==5):
        print("5.delete an existing element from the list:")
        element=(input("enter the element you want to delete:"))
        a.remove(element)
    elif(ch==6):
        print("6.delete an existing element from it's position:")
        index=int(input("enter the index of the element you want to delete:"))
        a.pop(index)
    elif(ch==7):
        print("7.sort the list in ascending order :")
        a.sort()
    elif(ch==8):
        print("8.display the list:",a)
        break
    else:
        print("Invalid choice! Please try again.")




        break
    
    




 
